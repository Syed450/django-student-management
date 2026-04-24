from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import studentserializer
from .models import student
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
# ---------------- FRONTEND VIEWS ----------------
@login_required(login_url='/user_login/')
def add_student(request):
    if request.method == "POST":
        student.objects.create(
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone")
        )
        return redirect('/students/')
    return render(request, "addstudent.html")


@login_required(login_url='/user_login/')
def student_list(request):
    data = student.objects.all()
    return render(request, "data.html", {"data": data})

@login_required(login_url='/user_login/')
def edit_student(request, id):
    data = get_object_or_404(student, id=id)

    if request.method == "POST":
        data.name = request.POST.get("name")
        data.age = request.POST.get("age")
        data.email = request.POST.get("email")
        data.phone = request.POST.get("phone")
        data.save()
        return redirect('/students/')

    return render(request, "edit.html", {"data": data})

@login_required(login_url='/user_login/')
def delete_student_view(request, id):
    student.objects.filter(id=id).delete()
    return redirect('/students/')


# ---------------- AUTH ----------------
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful. Please login.")
            return redirect('user_login')

    return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect('/students/')
        else:
            messages.error(request, "Invalid credentials")
            messages.error(request,"if account doesn't exist create a account by using registration")
            return render(request, "login.html")  # ✅ FIX

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('/user_login/')


# ---------------- API (FOR FRONTEND JS) ----------------
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def students_api(request):

    # GET ALL STUDENTS
    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentserializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE STUDENT
    if request.method == 'POST':
        serializer = studentserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------- UPDATE ----------------
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_student(request, id):
    try:
        student_obj = student.objects.get(id=id)
    except student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    serializer = studentserializer(student_obj, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


# ---------------- DELETE ----------------
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_student(request, id):
    try:
        student_obj = student.objects.get(id=id)
        student_obj.delete()
        return Response({"message": "Student deleted successfully"})
    except student.DoesNotExist:
        return Response({"error": "Student not found"})
