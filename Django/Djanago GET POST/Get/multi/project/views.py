from django.shortcuts import render

# Create your views here.

def multiplication(request):
    try:
        a=int(request.GET['m1'])
        b=int(request.GET['m2'])
        ans=a*b
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')
    