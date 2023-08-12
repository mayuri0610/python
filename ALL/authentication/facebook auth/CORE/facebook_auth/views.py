from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', locals())









