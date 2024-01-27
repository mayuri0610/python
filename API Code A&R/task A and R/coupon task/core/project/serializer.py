from rest_framework import serializers
from .models import *


class UserMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserMaster
        fields="__all__"


class CouponMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CouponMaster
        fields="__all__"
  

class AssignMasterSerializer(serializers.ModelSerializer):
    coupon=serializers.SerializerMethodField()
    user=serializers.SerializerMethodField()
    class Meta:
        model=AssignMaster
        fields=[ "id","coupon", "user"]

    def get_coupon(self, obj):
        couponobj = CouponMaster.objects.get(id = obj.coupon.id)
        return couponobj.coupon_name

    def get_user(self, obj):
        userobj=UserMaster.objects.get(id=obj.user.id)
        return userobj.username


class UsageMasterSerializer(serializers.ModelSerializer):
    coupon=serializers.SerializerMethodField()
    user=serializers.SerializerMethodField()
    class Meta:
        model=UsageMaster
        fields=[ "coupon", "user","date_usage" ]

    def get_coupon(self, obj):
        couponobj = CouponMaster.objects.get(id = obj.coupon.id)
        return couponobj.coupon_name

    def get_user(self, obj):
        userobj=UserMaster.objects.get(id=obj.user.id)
        return userobj.username


