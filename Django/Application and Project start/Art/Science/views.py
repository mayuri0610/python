from django.shortcuts import render

# Create your views here.

def fun_name(request):
    return render(request,'index.html')