from django.urls import path
from . views import *


urlpatterns = [


    path('PropertyMasterAPI/',PropertyMasterAPI.as_view(),name='PropertyMasterAPI'),
    path('PropertyMasterAPI/<int:id>',PropertyMasterAPI.as_view(),name='PropertyMasterAPI'),

    path('PropertyImageMasterAPI/',PropertyImageMasterAPI.as_view(),name='PropertyImageMasterAPI'),
    path('PropertyImageMasterAPI/<int:id>',PropertyImageMasterAPI.as_view(),name='PropertyImageMasterAPI'),

    path('AmenityMasterAPI/',AmenityMasterAPI.as_view(),name='AmenityMasterAPI'),
    path('AmenityMasterAPI/<int:id>',AmenityMasterAPI.as_view(),name='AmenityMasterAPI'),

    path('PropertyAmenityMasterAPI/',PropertyAmenityMasterAPI.as_view(),name='PropertyAmenityMasterAPI'),
    path('PropertyAmenityMasterAPI/<int:id>',PropertyAmenityMasterAPI.as_view(),name='PropertyAmenityMasterAPI'),

]