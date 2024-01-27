from rest_framework import serializers
from .models import *



class PropertyMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model=PropertyMaster
        fields= "__all__"


class PropertyImageMasterSerializer(serializers.ModelSerializer):

    class Meta:
            model=PropertyImageMaster
            fields= "__all__"


class AmenityMasterSerializer(serializers.ModelSerializer):

    class Meta:
            model=AmenityMaster
            fields= "__all__"



class PropertyAmenityMasterSerializer(serializers.ModelSerializer):

    property=serializers.SerializerMethodField()
    amenity=serializers.SerializerMethodField()

    class Meta:
            model=PropertyAmenityMaster
            fields= ["property","amenity","value"]

    def get_property(self, obj):
        obj = PropertyMaster.objects.get(id = obj.property.id)
        return obj.property_name

    def get_amenity(self, obj):
        obj = AmenityMaster.objects.get(id = obj.amenity.id)
        return obj.Amenity_name

