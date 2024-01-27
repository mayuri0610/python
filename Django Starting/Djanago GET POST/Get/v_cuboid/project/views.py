from django.shortcuts import render

# Create your views here.

def cuboid(request):
    try:
        n1=int(request.GET['v1'])
        n2=int(request.GET['v2'])
        n3=int(request.GET['v3'])
        ans=n1*n2*n3
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')


