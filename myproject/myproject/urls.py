from django.contrib import admin
from django.urls import path
from opp1.views import (
    add_student,
    student_list,
    edit_student,
    delete_student_view,
    register,
    user_login,
    user_logout,
    students_api,
    update_student,
    delete_student
)

urlpatterns = [
    path('', user_login, name='home'),
    path('admin/', admin.site.urls),
    # Authentication
    path('register/', register),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout),


    # Frontend
    path('add_student/', add_student),
    path('students/', student_list),
    path('edit_student/<int:id>/', edit_student),
    path('delete_student/<int:id>/', delete_student_view),

    # API
    path('api/students/', students_api),
    path('api/update/<int:id>/', update_student),
    path('api/delete/<int:id>/', delete_student),
]