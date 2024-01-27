from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from . import util

class PropertyMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            property_name=request.POST.get('property_name')
            property_discription=request.POST.get('property_discription')
            property_price=request.POST.get('property_price')
            property_location=request.POST.get('property_location')
            property_main_image=request.FILES.get('property_main_image')

            if property_name is not None and property_discription is not None and property_price is not None and property_location is not None and property_main_image is not None:
                if PropertyMaster.objects.filter( property_name=property_name,property_location=property_location).exists():
                    return Response(util.error(self,'property already register.'))
                else:
                    PropertyMaster.objects.create(property_name=property_name,property_discription=property_discription,property_price=property_price,property_location=property_location,property_main_image=property_main_image)
                    return Response(util.success(self,'Property is successfully created.'))
            else:
                return Response(util.error(self,'property_name and property_discription,property_price,property_location,property_main_image is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e)))

    def delete(self, request, id=None, format=None):
        try:
            if id is not None:
                try:
                    propertyobj = PropertyMaster.objects.get(id=id)
                    propertyobj.delete()
                    return Response(util.success(self,"Property deleted successfully"))
                except PropertyMaster.DoesNotExist:
                    return Response(util.error(self, "Property Id Not Match"))
            else:
                return Response(util.error(self, 'Property ID not provided.'))
        except Exception as e:
            return Response(util.error(self, str(e)))
        
    def get(self, request, format=None,id=None):
        try:
            if id is not None :
                try:
                    propertyobj = PropertyMaster.objects.get(id=id)
                    propertyserializer=PropertyMasterSerializer(propertyobj)

                    propertyimgobj=PropertyImageMaster.objects.filter(property=propertyobj)
                    propertyimageserializer=PropertyImageMasterSerializer(propertyimgobj, many=True)

                    propertyamenityobj=PropertyAmenityMaster.objects.filter(property=propertyobj)
                    propertyamenityserializer=PropertyAmenityMasterSerializer(propertyamenityobj, many=True)


                    property_data={
                        "Property": propertyserializer.data,
                        "Image":propertyimageserializer.data,
                        "Amenity":propertyamenityserializer.data
                    }

                    return Response(property_data)                
                except PropertyMaster.DoesNotExist:
                    return Response(util.error(self, "Property Id Not Match"))
            else:
                return Response(util.error(self, 'Property ID not provided.'))
        except Exception as e:
            return Response(util.error(self, str(e)))

    def put(self, request, format=None,id=None):
        try:
            if id is not None:
                try:
                    propertyobj= PropertyMaster.objects.get(id=id)
                    property_name=request.POST.get('property_name')
                    property_discription=request.POST.get('property_discription')
                    property_price=request.POST.get('property_price')
                    property_location=request.POST.get('property_location')
                    property_main_image=request.FILES.get('property_main_image')


                    if property_name !=None :
                        if PropertyMaster.objects.filter(property_name=property_name).exists():
                            pass
                        else:
                            propertyobj.property_name=property_name
                    
                    if property_discription != None :
                        propertyobj.property_discription=property_discription

                    if property_price != None :
                        propertyobj.property_price=property_price

                    if property_location != None :
                        propertyobj.property_location=property_location

                    if property_main_image != None :
                        propertyobj.property_main_image=property_main_image

                    propertyobj.save()
                    return Response(util.success(self,"Property update successfully"))

                except PropertyMaster.DoesNotExist:
                    return Response(util.error(self, "Property Id Not Match"))  
            else:          
                return Response(util.error(self, 'Property ID not provided.'))
        except Exception as e:
            return Response(util.error(self, str(e)))



class PropertyImageMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            propertyid=request.POST.get('propertyid')
            property_image=request.FILES.get('property_image')

            if propertyid is not None and property_image is not None:

                if PropertyMaster.objects.filter(id=propertyid):
                    propertyobj = PropertyMaster.objects.get(id=propertyid)
                    PropertyImageMaster.objects.create(property=propertyobj,property_image=property_image)
                    return Response(util.success(self,'Property image is successfully created.'))
                else: 
                    return Response(util.error(self, "Property Id Not Match"))
            else:
                return Response(util.error(self,'propertyid and property_image is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e)))
        

    def get(self, request, format=None,id=None):
            try:
                if id is None :
                    obj=PropertyImageMaster.objects.all()
                    serializerobj=PropertyImageMasterSerializer(obj, many=True)
                    return Response(serializerobj.data)
                else: 
                    return Response(util.error(self,'dont need id'))
            except Exception as e:
                return Response(util.error(self,str(e)))



class AmenityMasterAPI(APIView):
    def post(self, request,  format=None):
        try:
            vars = request.data
            Amenity_name=vars.get('Amenity_name')
    
            if Amenity_name is not None:
                if AmenityMaster.objects.filter(Amenity_name=Amenity_name).exists():
                    return Response(util.error(self, "Amenity is already in database."))
                else: 
                    AmenityMaster.objects.create(Amenity_name=Amenity_name)
                    return Response(util.success(self,'Amenity is successfully created.'))
            else:
                return Response(util.error(self,'Amenity_name is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e)))
        

    def get(self, request, format=None,id=None):
            try:
                if id is None :
                    obj=AmenityMaster.objects.all()
                    serializerobj=AmenityMasterSerializer(obj, many=True)
                    return Response(serializerobj.data)
                else: 
                    return Response(util.error(self,'dont need id'))
            except Exception as e:
                return Response(util.error(self,str(e)))
        



class PropertyAmenityMasterAPI(APIView):
    def post(self, request,  format=None):
        try:
            vars = request.data
            propertyid=vars.get('propertyid')
            amenityid=vars.get('amenityid')
            value=vars.get('value')
    
            if propertyid is not None and amenityid is not None and value is not None:
                if PropertyMaster.objects.filter(id=propertyid).exists():
                    if AmenityMaster.objects.filter(id=amenityid).exists():
                        propertyobj=PropertyMaster.objects.get(id=propertyid)
                        amenityobj=AmenityMaster.objects.get(id=amenityid)

                        if PropertyAmenityMaster.objects.filter(amenity=amenityobj).exists():
                            return Response(util.error(self, "Amenity is already taken for that property"))
                        else:
                            PropertyAmenityMaster.objects.create(property=propertyobj,amenity=amenityobj,value=value)
                            return Response(util.success(self,'Amenity added is successfully.'))
                    else:
                        return Response(util.error(self, "Amenity Id Not Match"))
                else: 
                    return Response(util.error(self, "Property Id Not Match"))
            else:
                return Response(util.error(self,' propertyid and amenityid and value is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e)))
        
    def get(self, request, format=None,id=None):
            try:
                if id is None :
                    obj=PropertyAmenityMaster.objects.all()
                    serializerobj=PropertyAmenityMasterSerializer(obj, many=True)
                    return Response(serializerobj.data)
                else: 
                    return Response(util.error(self,'dont need id'))
            except Exception as e:
                return Response(util.error(self,str(e)))


