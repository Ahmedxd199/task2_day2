"""lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Home, name='Home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='Home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapi/', include('myapi.urls')),
    path('contact', contact, name='contact'),
    path('', home, name='Home'),
    path('about', about, name='about'),
    path('register' , register , name="register"),
    path('login' , login , name="login"),
    path('userlogin', userlogin , name="userlogin"),
    path('logout', my_logout, name="my_logout"),
    path('deleteuser/<id>', deleteuser, name="deleteuser"),
    path('update/<id>', updateV, name="updateV"),
    # path('updateuser/<id>', updateuser , name="updateuser")
    path('Intake', insertIntake , name='intake'),
    path('SignUpForm1', insertForm1.as_view(), name='SignUpForm1'),
    path('SignUpForm2Model', insertForm2Model.as_view(), name='SignUpForm2Model'),
    path('Intakelist', Intakelist.as_view(), name='Intakelist'),


]
