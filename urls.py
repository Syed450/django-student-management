"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from opp1.views import add,multi,multiple,show,filter,get,filter1,add_student,edit_student,delete_data,register,user_login,user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',add),
    path('multi/',multi),
    path('multiple/',multiple),
    path('show/',show),
    path('filter/',filter),
    path('get/',get),
    path('filter1/',filter1),
    path('add_student/',add_student),
    path('edit_student/<int:id>/',edit_student),
    path('delete_data/<int:id>/',delete_data),
    path('register/',register),
    path('user_login/',user_login),
    path('user_logout/',user_logout),
]
