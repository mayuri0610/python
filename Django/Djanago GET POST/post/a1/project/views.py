from django.shortcuts import render

# Create your views here.

def square(request):
    if request.method == 'POST':
        try:
            a=int(request.POST['x'])
            b=int(request.POST['y'])
            ans=a*a+2*a*b+b*b
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')