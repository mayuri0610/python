from django.shortcuts import render

# Create your views here.
def square(request):
    try:
        num1=int(request.GET['side'])
        ans=num1*num1
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')


