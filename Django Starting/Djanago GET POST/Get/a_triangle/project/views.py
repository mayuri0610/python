from django.shortcuts import render

# Create your views here.

def triangle(request):
    try:
        num1=int(request.GET['base'])
        num2=int(request.GET['height'])
        ans=0.5*num1*num2
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')

