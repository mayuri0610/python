from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from .import util
# from .paginetor import MyPagination
from rest_framework import status



# Create your views here.

class UserMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            vars = request.data
            username = vars.get('username')

            if username is not None:
                UserMaster.objects.create(username=username)
                return Response(util.success(self,'User is successfully created'))
            else:
                return Response(util.error(self,'username needed'))
        except Exception as e:
            return Response(util.error(self,str(e))) 


    def get(self, request, format=None, id=None):
        try:
            user = UserMaster.objects.get(id=id)
            assignobj=AssignMaster.objects.filter(user=id) # mayuri assign coupon new10 and new20
            usageobj=UsageMaster.objects.filter(user=id)     # usage all

            print(user)
            print(assignobj)
            l=[]
            for i in assignobj:             # new10  new20      

                if i.coupon.per_usages > (UsageMaster.objects.filter(user=i.user) and UsageMaster.objects.filter(coupon=i.coupon)).count():
                    l.append(i)

            userserializer=UserMasterSerializer(user)
            assignserializer=AssignMasterSerializer(l,many=True)

            assign_usages={
                "user":userserializer.data,
                "assign coupon": assignserializer.data
            }
            

            return Response(assign_usages)
        except Exception as e:
            return Response(util.error(self, str(e)))

    def delete(self, request, format=None,id=None):
        try:
            if id is not None:
                if UserMaster.objects.filter(id=id):
                    obj=UserMaster.objects.get(id=id)
                    obj.delete()
                    return Response(util.success(self,'User is successfully deleted'))
                else:
                    return Response(util.error(self,"user Id Not Match"))
            else :
                return Response(util.error(self,'id is not valid'))
                # return Response(util.error(self,))
        except Exception as e:
            return Response(util.error(self,str(e))) 

    

class CouponMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            vars = request.data
            coupon_name = vars.get('coupon_name')
            invoice_type = vars.get('invoice_type')
            discount = vars.get('discount')
            per_usages = vars.get('per_usages')

            if coupon_name is not None and invoice_type is not None and discount is not None and per_usages is not None:
                CouponMaster.objects.create(coupon_name=coupon_name, invoice_type=invoice_type, discount=discount, per_usages=per_usages)
                return Response(util.success(self,'Coupon is successfully created'))
            else:
                return Response(util.error(self,'coupon_name and invoice_type and discount and per_usages is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e))) 
        
    def get(self, request, format=None,id=None):
        try:
            if id is None :
                obj=CouponMaster.objects.all()
                serializerobj=CouponMasterSerializer(obj, many=True)
                return Response(serializerobj.data)
            else :
                if CouponMaster.objects.filter(id=id):
                    obj=CouponMaster.objects.get(id=id)
                    serializerobj=CouponMasterSerializer(obj).data
                    return Response(serializerobj)
                else:
                    return Response(util.error(self,'"coupon Id Not Match"'))
        except Exception as e:
            return Response(util.error(self,str(e))) 


class AssignMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            vars = request.data
            couponid = vars.get('couponid')
            userid = vars.get('userid')

            if couponid is not None and userid is not None:
                if CouponMaster.objects.filter(id=couponid).exists():
                    if UserMaster.objects.filter(id=userid).exists():
                        userobj=UserMaster.objects.get(id=userid)
                        couponobj=CouponMaster.objects.get(id=couponid)
                        AssignMaster.objects.create(coupon=couponobj,user=userobj)
                        return Response(util.success(self,'Assign Coupon is successfully created'))
                    else:
                        return Response(util.error(self,'User id not match.'))
                else:
                    return Response(util.error(self,'Coupon id not match.'))
            else:
                return Response(util.error(self,'couponid and userid is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e))) 

    def get(self, request, format=None,id=None):
            try:
                if id is None :
                    obj=AssignMaster.objects.all()
                    serializerobj=AssignMasterSerializer(obj, many=True)
                    return Response(serializerobj.data)
                else :
                    if AssignMaster.objects.filter(id=id):
                        obj=AssignMaster.objects.get(id=id)
                        userobj=UserMaster.objects.get(id=obj.user)
                        couponobj=CouponMaster.objects.get(id=obj.coupon)
                        ans = couponobj.per_usages
                        used_coupons = UsageMaster.objects.filter(user=userobj, coupon=couponobj).count()

                        if ans > used_coupons:
                            remaining_coupons = ans - used_coupons - 1
                            obj.coupon.per_usages=remaining_coupons
                            obj.save()

                        serializerobj=AssignMasterSerializer(obj).data
                        return Response(serializerobj)
                    else:
                        return Response(util.error(self,"assign Id Not Match"))
            except Exception as e:
                return Response(util.error(self,str(e))) 
            
    def delete(self, request, format=None,id=None):
            try:
                if id is not None:
                    if AssignMaster.objects.filter(id=id):
                        obj=AssignMaster.objects.get(id=id).delete()
                        return Response(util.success(self,"assign coupon is successfully deleted"))
                    else:
                        return Response(util.error(self,"assign Id Not Match"))
                else :
                    return Response(util.error(self,"id is not valid"))
            except Exception as e:
                return Response(util.error(self,str(e))) 
                    

        



class UsageMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            vars = request.data
            couponid = vars.get('couponid')
            userid = vars.get('userid')
            date_usage = vars.get('date_usage')

            if couponid is not None and userid is not None and date_usage is not None:
                if CouponMaster.objects.filter(id=couponid).exists():
                    if UserMaster.objects.filter(id=userid).exists():
                        userobj=UserMaster.objects.get(id=userid)
                        couponobj=CouponMaster.objects.get(id=couponid)
                        
                        if AssignMaster.objects.filter(user=userobj, coupon=couponobj).exists():
                            ans = couponobj.per_usages
                            used_coupons = UsageMaster.objects.filter(user=userobj, coupon=couponobj).count()
                            if ans > used_coupons:
                                UsageMaster.objects.create(coupon=couponobj, user=userobj, date_usage=date_usage)
                                return Response(util.success(self,'Coupon is successfully used.'))
                        else:
                            return Response(util.error(self,'Coupon is expired assign that user.'))
                        
                        return Response(util.success(self,'Coupon is expired successfully Used'))
                    else:
                        return Response(util.error(self,'User id not match.'))
                else:
                    return Response(util.error(self,'Coupon id not match.'))
            else:
                return Response(util.error(self,'couponid and userid is needed.'))
        except Exception as e:
            return Response(util.error(self,str(e)))







