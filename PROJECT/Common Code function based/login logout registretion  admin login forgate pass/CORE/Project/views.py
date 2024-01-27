from django.shortcuts import render,redirect

from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def regitretion(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                print('username allready exist')
                return redirect('/regitretion')
            elif User.objects.filter(email=email).exists():
                print('email allready exist')
                return redirect('/regitretion')
            else:
                User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                return redirect('/')
    return render(request,'regitretion.html')


def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/index')
            else:
                 return redirect('/')
    return render(request, 'login.html')


def logout(request):
    user=request.user
    auth.logout(request)
    return redirect('/')



# def forgatepass(request):


# def adminlogin(request):
