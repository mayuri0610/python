from django.urls import path
from . import views

urlpatterns = [
   path('',views.swap,name='form')
]