from django.urls import path
from .views import *

urlpatterns = [
    path('Studentview',Studentview.as_view(),name='home'),
    path('Studentview/<int:id>',Studentview.as_view(),name='home'),
    path('ProfileView',ProfileView.as_view(),name='home'),
    path('ProfileView/<int:id>',ProfileView.as_view(),name='home'),



]
