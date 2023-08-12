from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializers,ProfileSerializers



class Studentview(APIView):

    # *****************       Post method manual methods      *****************
    def post(self, request, format=None):
        var=request.data
        name =var.get('name')
        roll =var.get('roll')
        address =var.get('address')

        if name is not None and roll is not None and roll is not None :
            Student.objects.create(name=name, roll=roll, address=address)
            return Response("data is created successfully")
        else:
            return Response("data is not created")
        

    # **************       Post serializer methods   ****************

    # def post(self, request, format=None):

    #     var=request.data
    #     serializer=StudentSerializers(data=var)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response("data is created successfully")
    #     else:
    #         return Response("data is not created")
     
    

    def delete(self,request, format=None, id=None):

        studentobj=Student.objects.get(id=id).delete()
        # studentobj.delete()
        return Response("data is deleted successfully")
        # obj =Student.objects.filter(id=id)
        # if obj is not None:

        # else:
        #     return Response("id is not found")
       
        

    def put(self,request, format=None, id=None):
        obj=Student.objects.filter(id=id)
        if obj is not None:
            studentobj=Student.objects.get(id=id)
            var=request.data
            name =var.get('name')
            roll =var.get('roll')
            address =var.get('address')

            if name is not None:
                studentobj.name=name
            if roll is not None:
                studentobj.roll=roll
            if address is not None:
                studentobj.address=address
            
            studentobj.save()
            return Response("Update data succesfully")
        else:
            return Response("id not match")
        
    def get(self, request, format=None,id=None):
        if id is None:
            obj=Student.objects.all()
            serializer=StudentSerializers(obj, many=True)
            # print(serializer.data)
            return Response(serializer.data)
        else:
            obj=Student.objects.get(id=id)
            serializer=StudentSerializers(obj)
            # print(serializer.data)
            return Response(serializer.data)



class ProfileView(APIView):
    def get(self, request, format=None):
        object=Profile.objects.all()
        serializer=ProfileSerializers(object,many=True)
        print(serializer.data)
        # serializer=ProfileSerializers(Profile.objects.all(),many=True)
        return Response(serializer.data)


    def post(self, request,format=None):
 
        studentid=request.POST.get('studentid')
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        image=request.FILES['image']

        if name is not None and priority is not None and image is not None and studentid is not None:
            if Student.objects.filter(id=studentid).exists():
                stuobj=Student.objects.get(id=studentid)
                Profile.objects.create(student=stuobj,name=name,priority=priority,image=image)
                return Response("success")
            
        else:
            return Response("not successful")


    def delete(self,request,format=None,id=None):
        # if id is not None:
            obj = Profile.objects.filter(id=id)
            if obj is not None:
                profileobj=Profile.objects.get(id=id)
                profileobj.delete()
                return Response("success")
            else:
                return Response("id not match") 
        # else:
        #     obj = Profile.objects.all()
        #     obj.delete()
        #     return Response("Delete all data")

    def put(self,request,format=None,id=None):
        obj= Profile.objects.filter(id=id)
        if obj is not None:
            profileobj=Profile.objects.get(id=id)
            name=request.POST.get('name')
            priority=request.POST.get('priority')
            image=request.FILES['image']

            if name != None :
                profileobj.name=name
            if image != None :
                profileobj.image=image
            if priority != None :
                profileobj.priority=priority
            
            profileobj.save()
            return Response("Update profile successfully")
        else:
            return Response("id not match")





        









        
