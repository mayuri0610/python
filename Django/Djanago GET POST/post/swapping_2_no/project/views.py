from django.shortcuts import render

# Create your views here.

def swap(request):
    if request.method == "POST":
        try:
            num1=int(request.POST['num1'])
            num2=int(request.POST['num2'])
            ans=num1
            num1=num2
            num2=ans
            dict={'key1':num1,'key2':num2}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')
        