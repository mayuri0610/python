from django.urls import path
from . import views
urlpatterns = [
    path('',views.reverse,name='form')
]