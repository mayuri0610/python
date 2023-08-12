from django.urls import path
from . import views

urlpatterns = [
    path('',views.area_1,name='form')
]