from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .mypagination import MyPagination
from django.db.models import Q


# Create your views here.

class CountryMasterAPI(APIView):  
    
    def get(self, request, format = None):
        search = request.GET.get('search')
        if search:
            multiple_q = Q(country_name__icontains = search)
            # multiple_q = Q(country_name__startswith = search)
            # multiple_q = Q(country_name__endswith = search)
            countryobj = CountryMaster.objects.filter(multiple_q)
        else:
            countryobj = CountryMaster.objects.all()

        mypagination = MyPagination()
        paginated_queryset = mypagination.paginate_queryset(countryobj, request)
        countryserializersobj = CountryMasterSerializers(paginated_queryset, many=True)
        return Response(countryserializersobj.data)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        country_name=vars.get("country_name")
        is_active=vars.get("is_active")


        if position != None and country_name!=None and is_active!=None :
            if CountryMaster.objects.filter(country_name=country_name).exists():
                return Response("Country is already in database")
            else :
                CountryMaster.objects.create(position=position, country_name=country_name, is_active=is_active)
                return Response("Country is successfully created")
        else :
            return Response("Country is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = CountryMaster.objects.get(id=id)
        if obj is not None:
            countryobj=CountryMaster.objects.get(id=id).delete()
            return Response("Country is successfully deleted")
        else :
            return Response("Country is not Deleted")
        
        # countryobj=CountryMaster.objects.get(id=id).delete()
        # return Response("Country is successfully deleted")


    
    def put(self,request, format=None,id=None):
        if CountryMaster.objects.filter(id=id):
            countryobj=CountryMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            country_name=vars.get("country_name")
            is_active=vars.get("is_active")


            if country_name is not None :
                object=CountryMaster.objects.filter(country_name=country_name).exists()
                if object is False:
                    countryobj.country_name=country_name

            if position is not None :
                countryobj.position=position
            
            if is_active is not None :
                countryobj.is_active=is_active

            countryobj.save()
            return Response("Country is updated")
        else :
            return Response("Country not found")


class StateMasterAPI(APIView):
    def get(self, request, format=None):
        stateobj = StateMaster.objects.all()
        # serializersobj=StateMasterSerializers(stateobj, many=True).data
        # return Response(serializersobj)
        serializersobj=StateMasterSerializers(stateobj, many=True)
        return Response(serializersobj.data)
    
    def post(self, request, format=None):
        vars = request.data
        countryid=vars.get("countryid")    
        position=vars.get("position") 
        state_name=vars.get("state_name")
        is_active=vars.get("is_active")

        if countryid!=None and position!=None and state_name!=None and is_active!=None :
            obj=CountryMaster.objects.filter(id=countryid).exists()
            if obj is True:
                if StateMaster.objects.filter(state_name=state_name).exists():
                    return Response("State is already in database")
                else:  
                    countryobj=CountryMaster.objects.get(id=countryid)
                    StateMaster.objects.create(country=countryobj, position=position, state_name=state_name, is_active=is_active)
                    return Response("State is successfully created")
            else:
                return Response("Country not found")
        else :
            return Response("State is not Created")
        
    def delete(self, request, format=None, id=None):
        obj=StateMaster.objects.filter(id=id)
        if obj is not None:
            stateobj=StateMaster.objects.get(id=id).delete()
            return Response("State is successfully deleted")
        else:
            return Response("State is not Deleted")
        
    def put(self,request, format=None,id=None):
        
        if StateMaster.objects.filter(id=id):
            obj = StateMaster.objects.get(id=id)
            vars = request.data
            position=vars.get("position")
            state_name=vars.get("state_name")
            is_active=vars.get("is_active")

            if position != None :
                obj.position=position

            if state_name !=None :
                object=StateMaster.objects.filter(state_name=state_name).exists()
                if object is False:
                    obj.state_name=state_name

            if is_active != None:
                obj.is_active=is_active

            obj.save()
            return Response("State is successfully updated")
        else:
            return Response("State is not found")


class CityMasterAPI(APIView):
    def get(self, request, format=None):
        cityobj = CityMaster.objects.all()
        cityserializerobj = CityMasterSerializers(cityobj, many=True)
        return Response(cityserializerobj.data)

    def post(self, request, format=None):
        vars = request.data
        stateid=vars.get('stateid')
        position=vars.get('position')
        city_name=vars.get('city_name')
        is_active=vars.get('is_active')

        if stateid !=None and position != None and city_name != None and is_active != None :
            # obj = StateMaster.objects.filter(id=stateid).exists()    # ye true or false me answer deta hai 
            if StateMaster.objects.filter(id=stateid).exists():
                if CityMaster.objects.filter(city_name=city_name).exists():
                    return Response("City is already in database")
                else:
                    CityMaster.objects.create(state=stateid,position=position, city_name=city_name, is_active=is_active)
                    return Response("City is successfully created")
            else:
                return Response("State not found")
        else:
            return Response("City is not Created")


    def delete(self, request, format=None, id=None):
        cityobj=CityMaster.objects.get(id=id).delete()
        # cityobj=CityMaster.objects.get(id=id)
        # cityobj.delete()
        return Response("City is successfully deleted")
    
    def put(self,request, format=None, id=None):
        if CityMaster.objects.filter(id=id) :
            cityobj=CityMaster.objects.get(id=id)
            vars = request.data
            position=vars.get('position')
            city_name=vars.get('city_name')
            is_active=vars.get('is_active')

            if position is not None :
                cityobj.position=position

            if city_name is not None :
                object=CityMaster.objects.filter(city_name=city_name).exists()
                if object is False:
                    cityobj.city_name=city_name


            if is_active is not None :
                cityobj.is_active=is_active
            
            cityobj.save()
            return Response("City is successfully updated")
        else :
            return Response("City is not available")


class EducationMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=EducationMaster.objects.all()
        serializers=EducationMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        education_name=vars.get("education_name")
        is_active=vars.get("is_active")


        if position != None and education_name!=None and is_active!=None :
            if EducationMaster.objects.filter(education_name=education_name).exists():
                return Response("Education is already in database")
            else :
                EducationMaster.objects.create(position=position, education_name=education_name, is_active=is_active)
                return Response("Education is successfully created")
        else :
            return Response("Education is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = EducationMaster.objects.get(id=id)
        if obj is not None:
            object=EducationMaster.objects.get(id=id).delete()
            return Response("Education is successfully deleted")
        else :
            return Response("Education is not Deleted")
        

    
    def put(self,request, format=None,id=None):
        if EducationMaster.objects.filter(id=id):
            obj=EducationMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            education_name=vars.get("education_name")
            is_active=vars.get("is_active")

            if position is not None :
                obj.position=position
            
            if education_name is not None :
                object=EducationMaster.objects.filter(education_name=education_name).exists()
                if object is False:
                    obj.education_name=education_name

            if is_active is not None :
                obj.is_active=is_active

            obj.save()
            return Response("Education is updated")
        else :
            return Response("Education not found")


class GenderMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=GenderMaster.objects.all()
        serializers=GenderMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        gender_name=vars.get("gender_name")
        is_active=vars.get("is_active")

        if position != None and gender_name!=None and is_active!=None :
            if GenderMaster.objects.filter(position=position, gender_name=gender_name).exists():
                return Response("Gender is already in database")
            else :
                GenderMaster.objects.create(position=position, gender_name=gender_name, is_active=is_active)
                return Response("Gender is successfully created")
        else :
            return Response("Gender is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = GenderMaster.objects.get(id=id)
        if obj is not None:
            object=GenderMaster.objects.get(id=id).delete()
            return Response("Gender is successfully deleted")
        else :
            return Response("Gender is not Deleted")
        
       


    
    def put(self,request, format=None,id=None):
        if GenderMaster.objects.filter(id=id):
            obj=GenderMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            gender_name=vars.get("gender_name")
            is_active=vars.get("is_active")

            if position is not None :
                obj.position=position
            if gender_name is not None :
                object=GenderMaster.objects.filter(gender_name=gender_name).exists()
                if object is False:
                    obj.gender_name=gender_name
            if is_active is not None :
                obj.is_active=is_active

            obj.save()
            return Response("Gender is updated")
        else :
            return Response("Gender not found")


class IcebreakMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=IcebreakMaster.objects.all()
        serializers=IcebreakMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        icebreak_name=vars.get("icebreak_name")
        is_active=vars.get("is_active")

        if position != None and icebreak_name!=None and is_active!=None :
            if IcebreakMaster.objects.filter(position=position, icebreak_name=icebreak_name).exists():
                return Response("Icebreaker is already in database")
            else :
                IcebreakMaster.objects.create(position=position, icebreak_name=icebreak_name, is_active=is_active)
                return Response("Icebreaker is successfully created")
        else :
            return Response("Icebreaker is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = IcebreakMaster.objects.get(id=id)
        if obj is not None:
            object=IcebreakMaster.objects.get(id=id).delete()
            return Response("Icebreaker is successfully deleted")
        else :
            return Response("Icebreaker is not Deleted")
        
       
    
    def put(self,request, format=None,id=None):
        if IcebreakMaster.objects.filter(id=id):
            obj=IcebreakMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            icebreak_name=vars.get("icebreak_name")
            is_active=vars.get("is_active")

            if position is not None :
                obj.position=position

            if icebreak_name is not None :
                object=IcebreakMaster.objects.filter(icebreak_name=icebreak_name).exists()
                if object is False:
                    obj.icebreak_name=icebreak_name
                
            if is_active is not None :
                obj.is_active=is_active

            obj.save()
            return Response("Icebreaker is updated")
        else :
            return Response("Icebreaker not found")


class PoliticalMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=PoliticalMaster.objects.all()
        serializers=PoliticalMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        political_name=vars.get("political_name")
        is_active=vars.get("is_active")

        if position != None and political_name!=None and is_active!=None :
            if PoliticalMaster.objects.filter(position=position, political_name=political_name).exists():
                return Response("Polotical Inclination is already in database")
            else :
                PoliticalMaster.objects.create(position=position, political_name=political_name, is_active=is_active)
                return Response("Polotical Inclination is successfully created")
        else :
            return Response("Polotical Inclination is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = PoliticalMaster.objects.get(id=id)
        if obj is not None:
            object=PoliticalMaster.objects.get(id=id).delete()
            return Response("Polotical Inclination is successfully deleted")
        else :
            return Response("Polotical Inclination is not Deleted")
        
       
    
    def put(self,request, format=None,id=None):
        if PoliticalMaster.objects.filter(id=id):
            obj=PoliticalMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            political_name=vars.get("political_name")
            is_active=vars.get("is_active")

            if position is not None :
                obj.position=position
            if political_name is not None :
                object=PoliticalMaster.objects.filter(political_name=political_name).exists()
                if object is False:
                    obj.political_name=political_name
            if is_active is not None :
                obj.is_active=is_active

            obj.save()
            return Response("Polotical Inclination is updated")
        else :
            return Response("Polotical Inclination not found")
        

class PromptsMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=PromptsMaster.objects.all()
        serializers=PromptsMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        prompts_name=vars.get("prompts_name")
        is_active=vars.get("is_active")


        if position != None and prompts_name!=None and is_active!=None :
            if PromptsMaster.objects.filter(position=position, prompts_name=prompts_name).exists():
                return Response("Prompts is already in database")
            else :
                PromptsMaster.objects.create(position=position, prompts_name=prompts_name, is_active=is_active)
                return Response("Prompts is successfully created")
        else :
            return Response("Prompts is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = PromptsMaster.objects.get(id=id)
        if obj is not None:
            object=PromptsMaster.objects.get(id=id).delete()
            return Response("Prompts is successfully deleted")
        else :
            return Response("Prompts is not Deleted")
        

    
    def put(self,request, format=None,id=None):
        if PromptsMaster.objects.filter(id=id):
            obj=PromptsMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            prompts_name=vars.get("prompts_name")
            is_active=vars.get("is_active")

            if position is not None :
                obj.position=position
            if prompts_name is not None :
                object=PromptsMaster.objects.filter(prompts_name=prompts_name).exists()
                if object is False:
                    obj.prompts_name=prompts_name
            if is_active is not None :
                obj.is_active=is_active
                
            obj.save()
            return Response("Prompts is updated")
        else :
            return Response("Prompts not found")


class LanguageMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=LanguageMaster.objects.all()
        serializers=LanguageMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        vars=request.data
        position=vars.get('position')
        language_name=vars.get("language_name")
        is_active=vars.get("is_active")


        if position != None and language_name!=None and is_active!=None :
            if LanguageMaster.objects.filter(position=position, language_name=language_name).exists():
                return Response("Language is already in database")
            else :
                LanguageMaster.objects.create(position=position, language_name=language_name, is_active=is_active)
                return Response("Language is successfully created")
        else :
            return Response("Language is not Created")
        
    def delete(self, request, format=None,id=None):
        obj = LanguageMaster.objects.get(id=id)
        if obj is not None:
            object=LanguageMaster.objects.get(id=id).delete()
            return Response("Language is successfully deleted")
        else :
            return Response("Language is not Deleted")
        

    
    def put(self,request, format=None,id=None):
        if LanguageMaster.objects.filter(id=id):
            obj=LanguageMaster.objects.get(id=id)
            vars=request.data
            position=vars.get('position')
            language_name=vars.get("language_name")
            is_active=vars.get("is_active")

            if language_name is not None :
                object=LanguageMaster.objects.filter(language_name=language_name).exists()
                if object is False:
                    obj.language_name=language_name
                

            if position is not None :
                    obj.position=position
            
            if is_active is not None :
                obj.is_active=is_active

            obj.save()
            return Response("Language is updated")
        else :
            return Response("Language not found")



class InterestMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=InterestMaster.objects.all()
        serializers=InterestMasterSerializers(obj,many=True).data
        return Response(serializers)

    def post(self, request, format=None):
        position=request.POST.get('position')
        interest_name=request.POST.get('interest_name')
        is_active=request.POST.get('is_active')
        blue_pic=request.FILES.get('blue_pic')
        grey_pic=request.FILES.get('grey_pic')

        if position != None and interest_name!=None and is_active!=None and blue_pic!=None and grey_pic!=None:
            if InterestMaster.objects.filter(interest_name=interest_name).exists():
                return Response("Interest is already in database")
            else :
                InterestMaster.objects.create(position=position, interest_name=interest_name, is_active=is_active, blue_pic=grey_pic, grey_pic=grey_pic)
                return Response("Interest is successfully created")
        else :
            return Response("Interest is not Created")
        
    def delete(self, request, format=None,id=None):
        if id is not None :
            obj = InterestMaster.objects.get(id=id)
            if obj is not None:
                object=InterestMaster.objects.get(id=id).delete()
                return Response("Interest is successfully deleted")
            else :
                return Response("Interest is not Deleted")
        else:
            obj = InterestMaster.objects.all()
            obj.delete()
            return Response("Interest is successfully deleted")
            

    
    def put(self,request, format=None,id=None):
        if InterestMaster.objects.filter(id=id):
            obj=InterestMaster.objects.get(id=id)

            position=request.POST.get('position')
            interest_name=request.POST.get('interest_name')
            is_active=request.POST.get('is_active')
            blue_pic=request.FILES.get('blue_pic')
            grey_pic=request.FILES.get('grey_pic')

            if interest_name is not None :
                object=InterestMaster.objects.filter(interest_name=interest_name).exists()
                if object is False:
                    obj.interest_name=interest_name

            if position is not None :
                obj.position=position
            if is_active is not None :
                obj.is_active=is_active
            if blue_pic is not None :
                obj.blue_pic=blue_pic
            if grey_pic is not None :
                obj.grey_pic=grey_pic

            obj.save()
            return Response("Interest is updated")
        else :
            return Response("Interest not found")


class PetsMasterAPI(APIView):  

    def get(self, request, format=None):
        obj=PetsMaster.objects.all()
        serializers=PetsMasterSerializers(obj,many=True).data
        return Response(serializers)


    def post(self, request, format=None):
        position=request.POST.get('position')
        pets_name=request.POST.get('pets_name')
        is_active=request.POST.get('is_active')
        blue_pic=request.FILES.get('blue_pic')
        grey_pic=request.FILES.get('grey_pic')

        if position != None and pets_name!=None and is_active!=None and blue_pic!=None and grey_pic!=None:
            if PetsMaster.objects.filter(pets_name=pets_name).exists():
                return Response("Pets is already in database")
            else :
                PetsMaster.objects.create(position=position, pets_name=pets_name, is_active=is_active, blue_pic=grey_pic, grey_pic=grey_pic)
                return Response("Pets is successfully created")
        else :
            return Response("Pets is not Created")



    def delete(self, request, format=None,id=None):
        if id is not None :
            obj = PetsMaster.objects.filter(id=id)
            if obj is not None:
                object=PetsMaster.objects.get(id=id).delete()
                return Response("Pets is successfully deleted")
            else :
                return Response("Pets is not Deleted")
        else:
            obj = PetsMaster.objects.all()
            obj.delete()
            return Response("Pets is successfully deleted")
            

    
    def put(self,request, format=None,id=None):
        if PetsMaster.objects.filter(id=id):
            obj=PetsMaster.objects.get(id=id)

            position=request.POST.get('position')
            pets_name=request.POST.get('pets_name')
            is_active=request.POST.get('is_active')
            blue_pic=request.FILES.get('blue_pic')
            grey_pic=request.FILES.get('grey_pic')

            if pets_name is not None :
                object=PetsMaster.objects.filter(pets_name=pets_name).exists()
                if object is False:
                    obj.pets_name=pets_name
                    

            if position is not None :
                obj.position=position
            if is_active is not None :
                obj.is_active=is_active
            if blue_pic is not None :
                obj.blue_pic=blue_pic
            if grey_pic is not None :
                obj.grey_pic=grey_pic

            obj.save()
            return Response("Pets is updated")
        else :
            return Response("Pets not found")



