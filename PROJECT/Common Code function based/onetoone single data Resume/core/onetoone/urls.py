from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("regitretion", views.regitretion, name="regitretion"),
    path("index", views.index, name="index"),
    path("form", views.form, name="form"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("active/<int:id>", views.active, name="active"),
    path("deactive/<int:id>", views.deactive, name="deactive"),

]
