from django.db import models

# Create your models here.
class Country_master(models.Model):
    position=models.IntegerField()
    country_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)


class Education_master(models.Model):
    position=models.IntegerField()
    education_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class State_master(models.Model):
    country=models.ForeignKey(Country_master,on_delete=models.CASCADE)
    position=models.IntegerField()
    state_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class Gender_master(models.Model):
    position=models.IntegerField()
    gender_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class Icebreak_master(models.Model):
    position=models.IntegerField()
    icebreak_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class Interest_master(models.Model):
    position=models.IntegerField()
    interest_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    blue_pic=models.ImageField(upload_to='blue icon',blank=True,null=True)
    grey_pic=models.ImageField(upload_to='grey icon',blank=True,null=True)

class Pets_master(models.Model):
    position=models.IntegerField()
    pets_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    blue_pic=models.ImageField(upload_to='blue icon',blank=True,null=True)
    grey_pic=models.ImageField(upload_to='grey icon',blank=True,null=True)


class  Political_master(models.Model):
    position=models.IntegerField()
    political_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class Prompts_master(models.Model):
    position=models.IntegerField()
    prompts_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class language_master(models.Model):
    position=models.IntegerField()
    language_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class City_master(models.Model):
    state=models.ForeignKey(State_master,on_delete=models.CASCADE)
    position=models.IntegerField()
    city_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)



