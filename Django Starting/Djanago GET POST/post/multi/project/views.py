from django.shortcuts import render

# Create your views here.

def multiplication(request):
    if request.method == 'POST':
        try:
            num1=int(request.POST['m1'])
            num2=int(request.POST['m2'])
            ans=num1*num2
            dict={'ans':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')


