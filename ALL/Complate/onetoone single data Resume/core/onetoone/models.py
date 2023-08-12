from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(to=User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    roll = models.IntegerField()
    aadhar_no= models.IntegerField()
    status = models.BooleanField(null= True, default=True, blank= True)





