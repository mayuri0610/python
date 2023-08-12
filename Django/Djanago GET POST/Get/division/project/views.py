from django.shortcuts import render

# Create your views here.

def div(request):
    try:
        num1=int(request.GET['d1'])
        num2=int(request.GET['d2'])
        ans=num1/num2
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')