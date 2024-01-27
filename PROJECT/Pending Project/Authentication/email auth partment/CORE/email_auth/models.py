from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User

# Create your models here.


class BaseContent(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # last_updated_by = models.ForeignKey(to=User , on_delete=models.CASCADE)

    class Meta:
        abstract = True

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
       
class UserAuth(AbstractBaseUser,  PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_login_by_social_login = models.BooleanField(default=False)
    is_two_factor_auth_active = models.BooleanField(default=False)
    is_referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    invited_referral_code = models.CharField(max_length=20, null=True, blank=True)
    login_count = models.PositiveIntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    otp=models.IntegerField(null=True,blank=True)
    otp_expire_at=models.DateTimeField(null=True,blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # No additional required fields


class ProfileTable(BaseContent):
    user_auth = models.OneToOneField(to=UserAuth,on_delete=models.CASCADE)
    # country_id = models.ForeignKey(to=Country,on_delete=models.CASCADE,blank=True, null=True)
    # state_id = models.ForeignKey(to=State,on_delete=models.CASCADE,blank=True, null=True)
    # city_id = models.ForeignKey(to=City,on_delete=models.CASCADE,blank=True, null=True)
    # profile_image = models.ImageField(upload_to='profile_images',blank=True,null=True)
    # first_name = models.CharField(max_length=40,null=True)
    # middle_name = models.CharField(max_length=40,null=True)
    # last_name = models.CharField(max_length=40,null=True)
    # phone_number_country_code = models.CharField(max_length=5,null=True)
    # phone_number = models.CharField(max_length=15,null=True)
    # zip_code = models.CharField(max_length=10)
    # home_address = models.TextField(blank=True, null=True)
    # date_of_birth = models.DateField(null=True, blank=True)
    # referral_code = models.CharField(max_length=20, null=True, blank=True)
    i_agree_on_terms_and_conditions = models.BooleanField(default=False)



class UserAuthLog(BaseContent):
    user_auth = models.OneToOneField(to=UserAuth, on_delete=models.CASCADE)
    action_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=50,blank=True, null=True)
    ip_location = models.CharField(max_length=100, blank=True, null=True)
    action_status = models.CharField(max_length=10,blank=True, null=True)
    action_remark = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=10)
    is_device_unknown = models.BooleanField(blank=True, null=True)
    is_location_unknown = models.BooleanField(blank=True, null=True)


class EmailLog(BaseContent):
    sent_to = models.EmailField()
    email_sent_status = models.BooleanField(default=False)
    unique_code = models.CharField(max_length=255) 
    expires_at = models.DateTimeField()
    email_type = models.CharField(max_length=255) 
    is_expired = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)


