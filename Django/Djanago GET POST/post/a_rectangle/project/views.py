from django.shortcuts import render

# Create your views here.

def rectangle(request):
    if request.method == "POST":
        try:
            num1=int(request.POST['length'])
            num2=int(request.POST['breadth'])
            ans=num1*num2
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')