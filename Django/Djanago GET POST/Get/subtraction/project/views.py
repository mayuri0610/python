from django.shortcuts import render

# Create your views here.

def fun(request):
    try:
        num1=int(request.GET['n1'])
        num2=int(request.GET['n2'])
        ans=num1-num2
        dict={'a1':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')
