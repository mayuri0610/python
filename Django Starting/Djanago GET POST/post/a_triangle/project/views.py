from django.shortcuts import render

# Create your views here.

def area_1(request):
    if request.method == "POST":
        try:
            num1=int(request.POST['base'])
            num2=int(request.POST['height'])
            ans=0.5*num1*num2
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')
