from django.shortcuts import render

# Create your views here.

def fun(request):
    try:
        a=int(request.GET['x'])
        b=int(request.GET['y'])       
        ans=(a+b)*(a+b)-(a-b)*(a-b)
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')
 