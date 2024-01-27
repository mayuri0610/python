from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class UserAuth(AbstractBaseUser):
    middle_name = models.CharField(max_length=40,null=True)
    phone_number_country_code = models.CharField(max_length=5,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    zip_code = models.CharField(max_length=10)
    home_address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    referral_code = models.CharField(max_length=20, null=True, blank=True)
    i_agree_on_terms_and_conditions = models.BooleanField(default=False)



#  Note 
#  AUTH_USER_MODEL = 'userapp.UserAuth'     written in settings