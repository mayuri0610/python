
from django.urls import path
from . import views


urlpatterns = [

    path('',views.adminlogin,name='login'),
    path('logout',views.logout,name='logout'),
    path('registretion',views.registretion,name='registretion'),
    path('all_book',views.all_book,name='all_book'),
    path('all_student',views.all_student,name='all_student'),


    # path('',views.adminlogin, name='adminlogin'),
    # path('index',views.index, name='index'),  

]
