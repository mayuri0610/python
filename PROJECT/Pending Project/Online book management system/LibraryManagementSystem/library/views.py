from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def adminlogin(request):

    return render(request, 'admin/login.html' )


def logout(request):
    user = request.user
    auth.logout(request)
    return redirect('adminlogin')


def registretion(request):

    return render(request, 'admin/register.html' )

def all_book(request):
    return render(request, 'admin/all_book.html' )

def all_student(request):
    return render(request, 'admin/all_student.html' )






# def adminlogin(request):
#     if request.method=='POST':
#         username=request.POST['email']
#         password=request.POST['password']

#         user=authenticate(username=username,password=password)

#         if user is not None:
#             if user.is_superuser ==True and user.is_active == True and user.is_staff == True:
#                 login(request,user)
#                 return redirect('index')
#             else:
#                 return redirect('/')
#         else:
#             return redirect('/')
    
#     return render(request, 'admin/login.html')



# @login_required(login_url = '/student_login')





