from django.shortcuts import render

# Create your views here.

def swap(request):
    try:
        num1=int(request.GET['n1'])
        num2=int(request.GET['n2'])
        ans=num1
        num1=num2
        num2=ans
        dict={'a1':num1,'a2':num2}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')