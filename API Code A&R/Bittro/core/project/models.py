from django.db import models

# Create your models here.

class CountryMaster(models.Model):
    position=models.IntegerField()
    country_name=models.CharField(max_length=100,null=True, blank=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.country_name 

class StateMaster(models.Model):
    country=models.ForeignKey(to=CountryMaster,on_delete=models.CASCADE)
    position=models.IntegerField()
    state_name=models.CharField(max_length=100,null=True, blank=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.state_name

class CityMaster(models.Model):
    state=models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    position=models.IntegerField() 
    city_name=models.CharField(max_length=100,null=True, blank=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.city_name



class EducationMaster(models.Model):
    position=models.IntegerField()
    education_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

def __str__(self):
        return self.education_name


class GenderMaster(models.Model):
    position=models.IntegerField()
    gender_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

def __str__(self):
        return self.gender_name

class IcebreakMaster(models.Model):
    position=models.IntegerField()
    icebreak_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

def __str__(self):
        return self.icebreak_name

class InterestMaster(models.Model):
    position=models.IntegerField()
    interest_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    blue_pic=models.ImageField(upload_to='Blue Icon',blank=True,null=True)
    grey_pic=models.ImageField(upload_to='Grey Icon',blank=True,null=True)

def __str__(self):
        return self.interest_name


class PetsMaster(models.Model):
    position=models.IntegerField()
    pets_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    blue_pic=models.ImageField(upload_to='Blue Icon',blank=True,null=True)
    grey_pic=models.ImageField(upload_to='Grey Icon',blank=True,null=True)

def __str__(self):
        return self.pets_name


class  PoliticalMaster(models.Model):
    position=models.IntegerField()
    political_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

def __str__(self):
        return self.political_name


class PromptsMaster(models.Model):
    position=models.IntegerField()
    prompts_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

def __str__(self):
        return self.prompts_name


class LanguageMaster(models.Model):
    position=models.IntegerField()
    language_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

def __str__(self):
        return self.language_name

