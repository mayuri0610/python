
from django.urls import path
from . import views
urlpatterns = [
   path('',views.km,name='form')
]