from django.urls import path
from . import views
urlpatterns = [
    path('',views.sign_in,name='sign_in'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('index',views.index,name='index'),
    path('location',views.location,name='location'),
    path('country_table',views.country_table,name='country_table'),
    path('add_country',views.add_country,name='add_country'),
    path('DeactiveCountry/<int:id>',views.DeactiveCountry,name='DeactiveCountry'),
    path('ActiveCountry/<int:id>',views.ActiveCountry,name='ActiveCountry'),
    path('country_delete/<int:id>',views.country_delete,name='country_delete'),
    path('country_update/<int:id>',views.country_update,name='country_update'),


    path('state_table',views.state_table,name='state_table'),

    path('add_state',views.add_state,name='add_state'),
    path('DeactiveState/<int:id>',views.DeactiveState,name='DeactiveState'),
    path('ActiveState/<int:id>',views.ActiveState,name='ActiveState'),
    path('state_delete/<int:id>',views.state_delete,name='state_delete'),
    path('state_update/<int:id>',views.state_update,name='state_update'),



     path('education_table',views.education_table,name='education_table'),
     path('add_education',views.add_education,name='add_education'),
     path('DeactiveEducation/<int:id>',views.DeactiveEducation,name='DeactiveEducation'),
     path('ActiveEducation/<int:id>',views.ActiveEducation,name='ActiveEducation'),
     path('education_delete/<int:id>',views.education_delete,name='education_delete'),
     path('education_update/<int:id>',views.education_update,name='education_update'),

     path('gender_table',views.gender_table,name='gender_table'),
     path('add_gender',views.add_gender,name='add_gender'),
     path('DeactiveGender/<int:id>',views.DeactiveGender,name='DeactiveGender'),
     path('ActiveGender/<int:id>',views.ActiveGender,name='ActiveGender'),
     path('gender_delete/<int:id>',views.gender_delete,name='gender_delete'),
     path('gender_update/<int:id>',views.gender_update,name='gender_update'),


     path('icebreak_table',views.icebreak_table,name='icebreak_table'),
     path('add_icebreak',views.add_icebreak,name='add_icebreak'),
     path('DeactiveIcebreak/<int:id>',views.DeactiveIcebreak,name='DeactiveIcebreak'),
     path('ActiveIcebreak/<int:id>',views.ActiveIcebreak,name='ActiveIcebreak'),
     path('icebreak_delete/<int:id>',views.icebreak_delete,name='icebreak_delete'),
     path('icebreak_update/<int:id>',views.icebreak_update,name='icebreak_update'),



    path('interest_table',views.interest_table,name='interest_table'),
    path('add_interest',views.add_interest,name='add_interest'),
    path('DeactiveInterest/<int:id>',views.DeactiveInterest,name='DeactiveInterest'),
    path('ActiveInterest/<int:id>',views.ActiveInterest,name='ActiveInterest'),
    path('interest_delete/<int:id>',views.interest_delete,name='interest_delete'),
    path('interest_update/<int:id>',views.interest_update,name='interest_update'),

    path('pets_table',views.pets_table,name='pets_table'),
    path('add_pets',views.add_pets,name='add_pets'),
    path('DeactivePets/<int:id>',views.DeactivePets,name='DeactivePets'),
    path('ActivePets/<int:id>',views.ActivePets,name='ActivePets'),
    path('pets_delete/<int:id>',views.pets_delete,name='pets_delete'),
    path('pets_update/<int:id>',views.pets_update,name='pets_update'),

    path('political_table',views.political_table,name='political_table'),
    path('add_political',views.add_political,name='add_political'),
    path('DeactivePolitical/<int:id>',views.DeactivePolitical,name='DeactivePolitical'),
    path('ActivePolitical/<int:id>',views.ActivePolitical,name='ActivePolitical'),
    path('political_delete/<int:id>',views.political_delete,name='political_delete'),
    path('political_update/<int:id>',views.political_update,name='political_update'),

     path('prompts_table',views.prompts_table,name='prompts_table'),
     path('add_prompts',views.add_prompts,name='add_prompts'),
     path('DeactivePrompts/<int:id>',views.DeactivePrompts,name='DeactivePrompts'),
     path('ActivePrompts/<int:id>',views.ActivePrompts,name='ActivePrompts'),
     path('prompts_delete/<int:id>',views.prompts_delete,name='prompts_delete'),
     path('prompts_update/<int:id>',views.prompts_update,name='prompts_update'),

     path('language_table',views.language_table,name='language_table'),
     path('add_language',views.add_language,name='add_language'),
     path('DeactiveLanguage/<int:id>',views.DeactiveLanguage,name='DeactiveLanguage'),
     path('ActiveLanguage/<int:id>',views.ActiveLanguage,name='ActiveLanguage'),
     path('language_delete/<int:id>',views.language_delete,name='language_delete'),
     path('language_update/<int:id>',views.language_update,name='language_update'),
     

     path('city_table',views.city_table,name='city_table'),
     path('add_city',views.add_city,name='add_city'),
     path('DeactiveCity/<int:id>',views.DeactiveCity,name='DeactiveCity'),
     path('ActiveCity/<int:id>',views.ActiveCity,name='ActiveCity'),
     path('city_delete/<int:id>',views.city_delete,name='city_delete'),
     path('city_update/<int:id>',views.city_update,name='city_update'),
    
     
]
