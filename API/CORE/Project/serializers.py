from rest_framework import serializers
from . models import *


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = "__all__"


class ProfileSerializers(serializers.ModelSerializer):
    student=StudentSerializers()
    class Meta:
        model =Profile
        fields = "__all__"
