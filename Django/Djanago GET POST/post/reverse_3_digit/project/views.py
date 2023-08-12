from django.shortcuts import render

# Create your views here.

def reverse(request):
    if request.method == 'POST':
        try:
            num1=int(request.POST['num'])
            i=0
            sum=0
            while(i<num1):
                num=num1%10
                sum=sum*10+num
                num1=num1//10
            dict={'key':sum}
            return render(request,'index.html',dict)
        except:
            return render(request,'index.html')
    else:
            return render(request,'index.html')
