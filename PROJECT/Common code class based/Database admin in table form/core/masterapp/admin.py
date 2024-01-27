from django.contrib import admin
from .models import *
# Register your models here.


# Type 1 

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name','code','currency','currency_symbol','is_state_available','slug')
    search_fields = ('id','name', 'code', 'currency')
    list_filter = ('is_active', 'is_state_available')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','country_id','state_name','slug')
    search_fields = ('state_name', 'id')
    list_filter = ('is_active',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','country_id','state_id','city_name','slug')
    search_fields = ('city_name', 'id')
    list_filter = ('is_active',)

# Type 2

class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'amenities_input_type', 'icon','is_filter_active','is_features','is_plural']
    search_fields = ['name', 'amenities_input_type']
    list_filter = ['is_filter_active', 'is_plural']

admin.site.register(Amenities, AmenitiesAdmin)

class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name'] 
    list_filter = ['is_active']

admin.site.register(FAQCategory, FAQCategoryAdmin)


# diffrence between type 1 and type 2

# type 1 
# tuple form     
# 1)  for single      list_filter = ('is_active',)      comma imp hai comma nahi diya to error aati hai
# 2)  @admin.register(Country)


# type 2 
# list form      
# for single      list_filter = ['is_active']          commom nah diya to bhi chalata hai
# admin.site.register(FAQCategory, FAQCategoryAdmin)


