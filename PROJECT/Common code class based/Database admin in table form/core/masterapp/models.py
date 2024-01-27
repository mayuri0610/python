from django.db import models

# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField
import uuid


class BaseContent(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # last_updated_by = models.ForeignKey(to=UserAuth , on_delete=models.CASCADE)

    class Meta:
        abstract = True


# Type 1

class Country(BaseContent):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10)
    currency = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=10)
    is_state_available = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,null=True)

    def __str__(self):
        return self.name
    

class State(BaseContent):
    country_id = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True)


    def __str__(self):
        return self.state_name

class City(BaseContent):
    state_id = models.ForeignKey(to=State, on_delete=models.CASCADE, null=True, blank=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.city_name





# Type 2

class Amenities(BaseContent):
    name = models.CharField(max_length=255, unique=True)
    amenities_input_type = models.CharField(max_length=255)
    icon = models.FileField(upload_to='amenities',null=True)
    is_filter_active = models.BooleanField(default=True)
    is_features = models.TextField(null=True)
    is_plural = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class FAQCategory(BaseContent):
    name = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name

class FAQAnswer(BaseContent):
    category_id=models.ForeignKey(to=FAQCategory,on_delete=models.CASCADE)
    question=models.TextField()
    answer=RichTextField()
    is_display = models.BooleanField(default=False)
    position = models.PositiveBigIntegerField()

    def __str__(self):
        return self.question

class Banner(BaseContent):
    banner_box=RichTextField(null=True, blank=True)

    def __str__(self):
        return self.banner_box
    

class UtilityCategory(BaseContent):
    category_name = models.CharField(max_length=255 )
    icon = models.FileField(upload_to= "utility_cayegory_icon")

    def __str__(self):
        return self.category_name
 
class RoleMasterCategory(BaseContent):
    role_master_category_name= models.CharField(max_length = 255)
    role_master_category_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField()

    def __str__(self):
        return self.role_master_category_name

class RoleMaster(BaseContent):
    role_master_category_id = models.ForeignKey(to=RoleMasterCategory ,on_delete = models.CASCADE)
    role_master_name = models.CharField(max_length = 255)
    role_master_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField()

    def __str__(self):
        return self.role_master_name

