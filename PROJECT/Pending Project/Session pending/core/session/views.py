from django.shortcuts import render

# Create your views here.

def setcookie(request):
    reponse = render(request,'student/setcookie.html' )
    reponse.set_cookie('name', 'Mayuri')
    return reponse

def getcookie(request):
    name = request.COOKIE['name']
    return render(request,'student/getcookie.html',{'name':name})   
