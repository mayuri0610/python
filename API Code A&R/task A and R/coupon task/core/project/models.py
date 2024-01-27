
from django.db import models

# Create your models here.

class UserMaster(models.Model):
    username = models.CharField(max_length=100,null=True, blank=True)

def __str__(self):
    return self.username


class CouponMaster(models.Model):
    coupon_name = models.CharField(max_length=100,null=True, blank=True)
    invoice_type = models.CharField(max_length=100,null=True,blank=True)       
    discount = models.DecimalField(max_digits=4,decimal_places=2, default=0.00)
    per_usages = models.IntegerField()


class AssignMaster(models.Model):
    coupon=models.ForeignKey(to=CouponMaster, on_delete=models.CASCADE)
    user=models.ForeignKey(to=UserMaster, on_delete=models.CASCADE)



class UsageMaster(models.Model):
    user=models.ForeignKey(to=UserMaster, on_delete=models.CASCADE)
    coupon=models.ForeignKey(to=CouponMaster, on_delete=models.CASCADE)
    date_usage=models.DateField(null=True,blank=True)



