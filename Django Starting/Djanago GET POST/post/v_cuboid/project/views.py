from django.shortcuts import render

# Create your views here.

def cuboid(request):
    if request.method == "POST":
        try:
            num1=int(request.POST['length'])
            num2=int(request.POST['breadth'])
            num3=int(request.POST['height'])
            ans=num1*num2*num3
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')
        