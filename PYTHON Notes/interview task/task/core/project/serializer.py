from rest_framework import serializers
from .models import *


class CategoryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryMaster
        fields="__all__"

class SubcategoryMasterSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    class Meta:
        model=SubCategoryMaster
        fields=[ "category", "id","subcategory_name","description" ]

    def get_category(self, obj):
        categoryobj = CategoryMaster.objects.get(id = obj.category.id)
        return categoryobj.category_name


class ReviewProductMasterSerializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    class Meta:
        model=ReviewProductMaster
        # fields="__all__"
        fields=["product","id","rating","comment","created_at"]

    def get_product(self, obj):
        productobj = ProductMaster.objects.get(id = obj.product.id)
        return productobj.product_name



class ProductMasterSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    subcategory=serializers.SerializerMethodField()

    # category=CategoryMasterSerializer()
    # subcategory=SubcategoryMasterSerializer()

    class Meta:
        model=ProductMaster
        # fields="__all__"
        fields=["category","subcategory","id","product_name","description","price","stock_quantity","main_image"]

    def get_category(self, obj):
        subcategoryobj = SubCategoryMaster.objects.get(id = obj.subcategory.id)
        categoryobj = CategoryMaster.objects.get(id=subcategoryobj.category.id)
        return categoryobj.category_name

    def get_subcategory(self, obj):
        subcategoryobj = SubCategoryMaster.objects.get(id = obj.subcategory.id)
        return subcategoryobj.subcategory_name
    




class ReviewProductMasterSerializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    class Meta:
        model=ReviewProductMaster
        # fields="__all__"
        fields=["product","id","rating","comment","created_at"]

    def get_product(self, obj):
        productobj = ProductMaster.objects.get(id = obj.product.id)
        return productobj.product_name
            
        
class ProductImageMasterSerializer(serializers.ModelSerializer):
    product=serializers.SerializerMethodField()
    class Meta:
        model=ProductImageMaster
        # fields="__all__"
        fields=["product","id","product_image"]

    def get_product(self, obj):
        productobj = ProductMaster.objects.get(id = obj.product.id)
        return productobj.id 
    
