from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate 
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Student



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


def index(request):
    user = request.user
    userobj = User.objects.get(id = user.id)
    if Student.objects.filter(user=userobj):
        studentobj = Student.objects.get(user=userobj)
    else:
        studentobj = None
    return render(request,'index.html',{'studentobj':studentobj})
   

def form(request):
    if request.method == 'POST':
        user = request.user
        name=request.POST['name']
        roll=request.POST['roll']
        aadhar_no=request.POST['aadhar_no']
        status=request.POST['status']

        Student.objects.create(user=user, name=name, roll=roll, aadhar_no=aadhar_no, status=status)
        return redirect('/index')

    return render(request,'form.html')

def active(request,id):
    obj=Student.objects.get(id=id)
    obj.status = True
    obj.save()
    return redirect('/index')

def deactive(request,id):
    obj=Student.objects.get(id=id)
    obj.status = False
    obj.save()
    return redirect('/index')


def delete(request,id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('/index')

def update(request,id):
    obj=Student.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['name']
        roll=request.POST['roll']
        aadhar_no=request.POST['aadhar_no']
        status=request.POST['status']

        obj.name=name
        obj.roll=roll
        obj.aadhar_no=aadhar_no
        obj.status=status

        obj.save()
        return redirect('/index')

    return render (request, 'update.html',{'obj':obj})


