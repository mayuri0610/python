from django.db import models

# Create your models here.

class Master(models.Model):
    student_name = models.CharField(max_length=100)
    roll_no = models.IntegerField()