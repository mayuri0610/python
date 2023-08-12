from django.shortcuts import render

# Create your views here.

def reverse(request):
    try:
        num1=int(request.GET['n1'])
        i=0
        rev=0
        while(i<num1):
            num=num1%10
            rev=rev*10+num
            num1=num1//10
        dict={'key':rev}
        return render(request,'index.html',dict)
    except:
        return render(request,'index.html')
    