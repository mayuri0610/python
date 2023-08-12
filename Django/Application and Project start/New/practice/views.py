from django.shortcuts import render

# Create your views here.
def fun(request):
    return render(request,'front_page.html')

def fun_name(request):
    return render(request,'index.html')

def fun_name2(request):
    return render(request,'table.html')
    