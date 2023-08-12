from django.shortcuts import render

# Create your views here.

def cube(request):
    try:
        a=int(request.GET['x'])
        b=int(request.GET['y'])
        c=int(request.GET['z'])
        ans=(a*a+b*b+c*c)+2*(a*b+b*c+c*a)
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')