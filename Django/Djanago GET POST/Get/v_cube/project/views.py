from django.shortcuts import render

# Create your views here.
def cube(request):
    try:
        n1=int(request.GET['side'])
        ans=n1*n1*n1
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')