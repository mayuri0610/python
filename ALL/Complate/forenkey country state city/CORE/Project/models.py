from django.db import models

# Create your models here.

class Country_model(models.Model):
    country_name = models.CharField(max_length=100)
    position = models.IntegerField()
    country_pic=models.ImageField(upload_to='Country pic',blank=True,null=True)
    status = models.BooleanField(null= True, default=True, blank= True)


class State_model(models.Model):
    country = models.ForeignKey(Country_model,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)
    position = models.IntegerField()
    state_pic=models.ImageField(upload_to='State pic',blank=True,null=True)
    status = models.BooleanField(null= True, default=True, blank= True)

class City_model(models.Model):
    state = models.ForeignKey(State_model,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    position = models.IntegerField()
    city_pic=models.ImageField(upload_to='City pic',blank=True,null=True)
    status = models.BooleanField(null= True, default=True, blank= True)