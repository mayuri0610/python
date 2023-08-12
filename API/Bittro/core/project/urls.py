
from django.urls import path
from .views import *


urlpatterns = [
    
    path('CountryMasterAPI',CountryMasterAPI.as_view(),name='CountryMasterAPI'),
    path('CountryMasterAPI/<int:id>',CountryMasterAPI.as_view(),name='CountryMasterAPI'),

    path('StateMasterAPI',StateMasterAPI.as_view(),name='StateMasterAPI'),
    path('StateMasterAPI/<int:id>',StateMasterAPI.as_view(),name='StateMasterAPI'),

    path('CityMasterAPI',CityMasterAPI.as_view(),name='CityMasterAPI'),
    path('CityMasterAPI/<int:id>',CityMasterAPI.as_view(),name='CityMasterAPI'),


    path('EducationMasterAPI',EducationMasterAPI.as_view(),name='EducationMasterAPI'),
    path('EducationMasterAPI/<int:id>',EducationMasterAPI.as_view(),name='EducationMasterAPI'),

    path('GenderMasterAPI',GenderMasterAPI.as_view(),name='GenderMasterAPI'),
    path('GenderMasterAPI/<int:id>',GenderMasterAPI.as_view(),name='GenderMasterAPI'),

    path('IcebreakMasterAPI',IcebreakMasterAPI.as_view(),name='IcebreakMasterAPI'),
    path('IcebreakMasterAPI/<int:id>',IcebreakMasterAPI.as_view(),name='IcebreakMasterAPI'),


    path('PoliticalMasterAPI',PoliticalMasterAPI.as_view(),name='PoliticalMasterAPI'),
    path('PoliticalMasterAPI/<int:id>',PoliticalMasterAPI.as_view(),name='PoliticalMasterAPI'),


    path('PromptsMasterAPI',PromptsMasterAPI.as_view(),name='PromptsMasterAPI'),
    path('PromptsMasterAPI/<int:id>',PromptsMasterAPI.as_view(),name='PromptsMasterAPI'),


    path('LanguageMasterAPI',LanguageMasterAPI.as_view(),name='LanguageMasterAPI'),
    path('LanguageMasterAPI/<int:id>',LanguageMasterAPI.as_view(),name='LanguageMasterAPI'),

    path('InterestMasterAPI',InterestMasterAPI.as_view(),name='InterestMasterAPI'),
    path('InterestMasterAPI/<int:id>',InterestMasterAPI.as_view(),name='InterestMasterAPI'),

    path('PetsMasterAPI',PetsMasterAPI.as_view(),name='PetsMasterAPI'),
    path('PetsMasterAPI/<int:id>',PetsMasterAPI.as_view(),name='PetsMasterAPI'),

    
]
