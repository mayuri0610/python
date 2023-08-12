from django.shortcuts import render

# Create your views here.

def circle(request):
    if request.method == "POST":
        try:
            num1=int(request.POST['radish'])
            ans=3.1452*num1*num1
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')
        

