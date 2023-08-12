
from rest_framework import serializers
from . models import *


class CountryMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =CountryMaster
        fields = "__all__"
        # fields = ["country_name"]

class StateMasterSerializers(serializers.ModelSerializer):
    country=CountryMasterSerializers()
    class Meta:
        model =StateMaster
        fields = "__all__"
        # fields = ["state_name","country"]




# serializers.SerializerMethodField()
class CityMasterSerializers(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    class Meta:
        model = CityMaster
        fields = [ "country", "state", "city_name"]

        # fields = "__all__"
    
    def get_country(self, obj):
        stateobj = StateMaster.objects.get(id = obj.state.id)
        countryobj = CountryMaster.objects.get(id=stateobj.country.id)
        return countryobj.country_name

    def get_state(self, obj):
        stateobj = StateMaster.objects.get(id = obj.state.id)
        return stateobj.state_name




class EducationMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =EducationMaster
        fields = "__all__"

class GenderMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =GenderMaster
        fields = "__all__"

class IcebreakMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =IcebreakMaster
        fields = "__all__"

class PoliticalMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =PoliticalMaster
        fields = "__all__"

class PromptsMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =PromptsMaster
        fields = "__all__"

class LanguageMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =LanguageMaster
        fields = "__all__"

class InterestMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =InterestMaster
        fields = "__all__"

class PetsMasterSerializers(serializers.ModelSerializer):
    class Meta:
        model =PetsMaster
        fields = "__all__"
