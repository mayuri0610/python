from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

# Create your views here.


def index(request):
    profileobj=profile.objects.all()
    if request.method == 'GET':
        st= request.GET.get('name')
        if st!= None:
            # profileobj=profile.objects.filter(name=st)    # full name
            profileobj=profile.objects.filter(name__icontains=st)   # dono side se search 


    return render(request,'index.html',{'profileobj':profileobj})


def form(request):
    if request.method=='POST':
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        profile.objects.create(name=name,roll_no=roll_no)
        return redirect('index')

    return render(request,'form.html')
