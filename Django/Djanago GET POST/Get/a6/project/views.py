from django.shortcuts import render

# Create your views here.

def fun(request):
    try:
        a=int(request.GET['x'])
        b=int(request.GET['y'])
        c=int(request.GET['z'])
        ans=(a+b+c)*(a+b+c)-(a*a+b*b+c*c)
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')