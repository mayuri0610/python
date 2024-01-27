from django.shortcuts import render

# Create your views here.

def fun(request):
    try:
        a=int(request.GET['x'])
        b=int(request.GET['y'])       
        ans=a*a*a+b*b*b+3*a*b*(a+b)  
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')
    