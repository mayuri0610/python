from django.shortcuts import render

# Create your views here.

def cube(request):
    
    if request.method == 'POST':
        try:
            a=int(request.POST['x'])
            b=int(request.POST['y'])
            c=int(request.POST['z'])
            ans=(a*a+b*b+c*c)+2*(a*b+b*c+c*a)
            dict={'key':ans}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
        return render(request,'index.html')