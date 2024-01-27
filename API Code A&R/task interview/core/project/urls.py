
from django.urls import path
from . views import *


urlpatterns = [

    path('CategoryMasterAPI',CategoryMasterAPI.as_view(),name='CategoryMasterAPI'),
    path('CategoryMasterAPI/<int:id>',CategoryMasterAPI.as_view(),name='CategoryMasterAPI'),

    path('SubCategoryMasterAPI',SubCategoryMasterAPI.as_view(),name='SubCategoryMasterAPI'),
    path('SubCategoryMasterAPI/<int:id>',SubCategoryMasterAPI.as_view(),name='SubCategoryMasterAPI'),
    

    path('ProductMasterAPI',ProductMasterAPI.as_view(),name='ProductMasterAPI'),
    path('ProductMasterAPI/<int:id>',ProductMasterAPI.as_view(),name='ProductMasterAPI'),

    path('ReviewProductMasterAPI',ReviewProductMasterAPI.as_view(),name='ReviewProductMasterAPI'),
    path('ReviewProductMasterAPI/<int:id>',ReviewProductMasterAPI.as_view(),name='ReviewProductMasterAPI'),

    path('ProductImageMasterAPI',ProductImageMasterAPI.as_view(),name='ProductImageMasterAPI'),
    path('ProductImageMasterAPI/<int:id>',ProductImageMasterAPI.as_view(),name='ProductImageMasterAPI'),
    
]
