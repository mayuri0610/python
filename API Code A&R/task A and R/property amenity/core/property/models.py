from django.db import models

# Create your models here.


class PropertyMaster(models.Model):
    property_name = models.CharField(max_length=250,null=True, blank=True)
    property_discription = models.TextField(null=True, blank=True)
    property_price = models.PositiveIntegerField(null=True, blank=True)
    property_location = models.TextField(null=True, blank=True)
    property_main_image = models.ImageField(upload_to="Property main image",null=True, blank=True)


class PropertyImageMaster(models.Model):
    property = models.ForeignKey(to=PropertyMaster, on_delete=models.CASCADE)
    property_image = models.ImageField(upload_to="Property image",null=True, blank=True)


class AmenityMaster(models.Model):
    Amenity_name = models.CharField(max_length=120,null=True,blank=True)


class PropertyAmenityMaster(models.Model):
    property = models.ForeignKey(to=PropertyMaster, on_delete=models.CASCADE)
    amenity = models.ForeignKey(to=AmenityMaster, on_delete=models.CASCADE)
    value=models.PositiveIntegerField(null=True,blank=True)

class CountryModel(models.Model):
    Price = models.CharField(max_length=120,null=True,blank=True)



