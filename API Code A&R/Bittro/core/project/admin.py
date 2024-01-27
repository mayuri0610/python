from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(CityMaster)

# @admin.register(CountryMaster)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ['id',"country_name","is_active"]
