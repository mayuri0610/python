from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        num1=int(request.GET['num1']) 
        num2=int(request.GET['num2']) 
        ans=num1+num2
        print(ans)
        contex={'ans':ans}
        return render(request,'index.html', contex)
    
    except:

        return render(request,'index.html')