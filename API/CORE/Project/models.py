from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField()
    address=models.CharField(max_length=200)



class Profile(models.Model):
    student= models.OneToOneField(to=Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    priority = models.IntegerField()
    image =models.ImageField(upload_to='images')
    