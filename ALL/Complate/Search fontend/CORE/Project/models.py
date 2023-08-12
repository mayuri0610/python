from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(default=True, null=True, blank=True)
