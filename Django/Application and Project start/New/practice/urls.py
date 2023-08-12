
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun,name='Hello'),
    path('form',views.fun_name,name='form'),
    path('form/table',views.fun_name2,name='table')
]


# urlpatterns = [
#     path('',views.fun,name='Hello'),
#     path('form',views.fun_name,name='form'),
#     path('table',views.fun_name2,name='table')
# ]

