from django.shortcuts import render

# Create your views here.

def tem_cel(request):
    if request.method == 'POST':
        try:
            num1=int(request.POST['num'])
            fah=1.8*num1+32
            dict={'tem':fah}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
            return render(request,'index.html')


