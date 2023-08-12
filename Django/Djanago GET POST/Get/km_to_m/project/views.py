from django.shortcuts import render

# Create your views here.

def meter(request):
    try:
        n1=int(request.GET['km'])
        ans=n1*1000
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')
