from django.shortcuts import render

# Create your views here.

def km(request):
    if request.method == 'POST':
        try:
            num1=int(request.POST['num'])
            ans=num1*1000
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')
