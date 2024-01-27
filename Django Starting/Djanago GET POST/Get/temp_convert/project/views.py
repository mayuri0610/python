from django.shortcuts import render

# Create your views here.

def meter(request):
    try:
        n1=int(request.GET['cel'])
        ans=1.8*n1+32
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')