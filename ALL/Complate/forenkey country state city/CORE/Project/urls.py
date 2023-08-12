
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('country_table',views.country_table,name='country_table'),
    path('country_add',views.country_add,name='country_add'),
    path('country_active/<int:id>',views.country_active,name='country_active'),
    path('country_deactive/<int:id>',views.country_deactive,name='country_deactive'),
    path('country_delete/<int:id>',views.country_delete,name='country_delete'),
    path('country_update/<int:id>',views.country_update,name='country_update'),

    path('state_table',views.state_table,name='state_table'),
    path('state_add',views.state_add,name='state_add'),
    path('state_active/<int:id>',views.state_active,name='state_active'),
    path('state_deactive/<int:id>',views.state_deactive,name='state_deactive'),
    path('state_delete/<int:id>',views.state_delete,name='state_delete'),
    path('state_update/<int:id>',views.state_update,name='state_update'),

    path('city_table',views.city_table,name='city_table'),
    path('city_add',views.city_add,name='city_add'),
    path('c/<int:id>',views.city_active,name='city_active'),
    path('city_deactive/<int:id>',views.city_deactive,name='city_deactive'),
    path('city_delete/<int:id>',views.city_delete,name='city_delete'),
    path('city_update/<int:id>',views.city_update,name='city_update'),



]