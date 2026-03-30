from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import student
def add(request):
    obj = student(name="syed harshad basha,",age= 21,email="syedharshad99@gmail.com",phone="6303948231")
    obj.save()
    return HttpResponse("done one record")
def multi(request):
    students = [
        student(name="hemanth", age=21, email="hemanth1@gmail.com", phone="9346402404"),
        student(name="arshad", age=22, email="arshad1@gmail.com", phone="9346402405"),
        student(name="kalyan", age=23, email="kalyan1@gmail.com", phone="9346402406"),
        student(name="rahul", age=20, email="rahul1@gmail.com", phone="9346402407"),
        student(name="sai", age=21, email="sai1@gmail.com", phone="9346402408"),
        student(name="vamsi", age=24, email="vamsi1@gmail.com", phone="9346402409"),
        student(name="praveen", age=22, email="praveen1@gmail.com", phone="9346402410"),
        student(name="naresh", age=23, email="naresh1@gmail.com", phone="9346402411"),
        student(name="manoj", age=21, email="manoj1@gmail.com", phone="9346402412"),
        student(name="ravi", age=22, email="ravi1@gmail.com", phone="9346402413"),
    ]

    student.objects.bulk_create(students)

    return HttpResponse("Inserted successfully")
def multiple(request):
    stu=[
        student(name="naresh", age=23, email="naresh1@gmail.com", phone="9346402411"),
        student(name="manoj", age=21, email="manoj1@gmail.com", phone="9346402412"),
        student(name="ravi", age=22, email="ravi1@gmail.com", phone="9346402413"),
    ]
    student.objects.bulk_create(stu)
    return HttpResponse("another time inserted")

def show(request):
    data= student.objects.all()
    return HttpResponse(data)
def filter(request):
    data = student.objects.filter(name="ravi")
    return HttpResponse(data)
def get(request):
    data = student.objects.get(age=23)
    return HttpResponse(data)
def filter1(request):
    data=student.objects.all()
    return render(request,"data.html",{"data":data})
def add_student(request):
    if request.method == "POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        email=request.POST.get("email")
        phone=request.POST.get("phone")

        student.objects.create(name=name,age=age,email=email,phone=phone)
        return render(request,"addstudent.html")
    return render(request,"addstudent.html")
def edit_student(request,id):
    data=student.objects.get(id=id)
    if request.method == "POST":
        data.name=request.POST.get("name")
        data.age=request.POST.get("age")
        data.email=request.POST.get("email")
        data.phone=request.POST.get("phone")
        data.save()
        return redirect('/filter1/')
    return render(request,"edit.html",{"data":data})
def delete_data(request,id):
    print("DELETE WORKING")
    data = student.objects.filter(id=id)
    data.delete()
    return redirect('/filter1/')
def register(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists")
        else:
            User.objects.create_user(username=username,password=password)
            messages.success(request,"user created suceessfully")
            return redirect('/user_login/')
    return render(request,"register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/filter1/')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "login.html")
def user_logout(request):
    logout(request)
    return redirect('/user_login/')
@login_required(login_url='/user_login/')
def filter1(request):
    data = student.objects.all()
    return render(request, "data.html", {"data": data})
 