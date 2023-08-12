from django.shortcuts import render

# Create your views here.
def circle(request):
    try:
        num1=int(request.GET['radius'])
        ans=3.1452*num1*num1
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')