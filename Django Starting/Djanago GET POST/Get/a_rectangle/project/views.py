from django.shortcuts import render

# Create your views here.

def rectangle(request):
    try:
        num1=int(request.GET['length'])
        num2=int(request.GET['breadth'])
        ans=num1*num2
        dict={'key':ans}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')

