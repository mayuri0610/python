
from django.urls import path
# from . import views
from das_admin import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('patient_list',views.patient_list,name='patient_list'),
    path('doctor_list',views.doctor_list,name='doctor_list'),
    path('appointment_list',views.appointment_list,name='appointment_list'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    path('doctor_deactive/<int:id>',views.doctor_deactive,name='doctor_deactive'),
    path('doctor_active/<int:id>',views.doctor_active,name='doctor_active'),



    path('blank_page',views.blank_page,name='blank_page'),
    path('components',views.components,name='components'),
    path('data_tables',views.data_tables,name='data_tables'),
    path('error_404',views.error_404,name='error_404'),
    path('error_500',views.error_500,name='error_500'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('form_basic_inputs',views.form_basic_inputs,name='form_basic_inputs'),
    path('form_horizontal',views.form_horizontal,name='form_horizontal'),
    path('form_input_groups',views.form_input_groups,name='form_input_groups'),
    path('form_mask',views.form_mask,name='form_mask'),
    path('form_validation',views.form_validation,name='form_validation'),
    path('form_vertical',views.form_vertical,name='form_vertical'),
    path('invoice_report',views.invoice_report,name='invoice_report'),
    path('invoice',views.invoice,name='invoice'),
    path('lock_screen',views.lock_screen,name='lock_screen'),
    path('reviews',views.reviews,name='reviews'),
    path('settings',views.settings,name='settings'),
    path('tables_basic',views.tables_basic,name='tables_basic'),
    path('transactions_list',views.transactions_list,name='transactions_list'),

]