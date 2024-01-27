from django.urls import path
from .views import *

urlpatterns = [


    path('UserMasterAPI',UserMasterAPI.as_view(),name='UserMasterAPI'),
    path('UserMasterAPI/<int:id>',UserMasterAPI.as_view(),name='UserMasterAPI'),
    
    path('CouponMasterAPI',CouponMasterAPI.as_view(),name='CouponMasterAPI'),
    path('CouponMasterAPI/<int:id>',CouponMasterAPI.as_view(),name='CouponMasterAPI'),
    
    path('AssignMasterAPI',AssignMasterAPI.as_view(),name='AssignMasterAPI'),
    path('AssignMasterAPI/<int:id>',AssignMasterAPI.as_view(),name='AssignMasterAPI'),
    
    path('UsageMasterAPI',UsageMasterAPI.as_view(),name='UsageMasterAPI'),
    path('UsageMasterAPI/<int:id>',UsageMasterAPI.as_view(),name='UsageMasterAPI'),
    

    
]