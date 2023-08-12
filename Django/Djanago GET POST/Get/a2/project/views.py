from django.shortcuts import render

# Create your views here.

def square(request):
    try:
        a=int(request.GET['x'])
        b=int(request.GET['y'])
        ans=a*a-2*a*b+b*b
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')