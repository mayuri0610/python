
from django.urls import path
from . import views
urlpatterns = [
    path('',views.tem_cel,name='form')
]