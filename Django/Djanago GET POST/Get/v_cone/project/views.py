from django.shortcuts import render

# Create your views here.

def cone(request):
    try:
        n1=int(request.GET['redius'])
        n2=int(request.GET['height'])
        ans=(3.1452*n1**n1*n2)/3
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')