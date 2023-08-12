from django.shortcuts import render

# Create your views here.

def sub(request):
    if request.method == "POST":
        try:
            num1=int(request.POST['s1'])
            num2=int(request.POST['s2'])
            ans=num1-num2
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')

