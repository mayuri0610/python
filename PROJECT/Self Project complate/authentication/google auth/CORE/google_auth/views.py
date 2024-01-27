from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', locals())




# <a href="{% url 'social:begin' 'google-oauth2' %}" class="alert-link">Clike Here </a>

    # path('social-auth/', include('social_django.urls' , namespace='social-auth')),

# provider_login_