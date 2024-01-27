from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("regitretion", views.regitretion, name="regitretion"),
    path("index", views.index, name="index"),

]
