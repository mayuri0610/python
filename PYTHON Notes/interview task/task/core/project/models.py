from django.db import models

# Create your models here.

class CategoryMaster(models.Model):
    category_name= models.CharField(max_length=250, blank=True,null=True,default=True)
    description= models.TextField(blank=True,null=True,default=True)
    
    def __str__(self):
        return self.category_name

class SubCategoryMaster(models.Model):
    category = models.ForeignKey(to=CategoryMaster, on_delete=models.CASCADE)
    subcategory_name= models.CharField(max_length=250, blank=True,null=True,default=True)
    description= models.TextField(blank=True,null=True,default=True)

    def __str__(self):
        return self.subcategory_name

class ProductMaster(models.Model):
    subcategory = models.ForeignKey(to=SubCategoryMaster, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=250, blank=True,null=True,default=True)
    description= models.TextField(blank=True,null=True,default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    main_image = models.ImageField(upload_to='Product Main Image',blank=True, null=True)

    def __str__(self):
        return self.product_name    

class ProductImageMaster(models.Model):
    product = models.ForeignKey(to=ProductMaster,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='Product Image',blank=True,null=True)
    
class ReviewProductMaster(models.Model):
    product = models.ForeignKey(to=ProductMaster,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True,null=True,default=True)
    created_at = models.DateTimeField(auto_now_add=True)


