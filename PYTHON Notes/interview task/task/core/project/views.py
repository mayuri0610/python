from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from .paginetor import MyPagination
from rest_framework import status


# Create your views here.
class CategoryMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            vars = request.data
            category_name = vars.get('category_name')
            description = vars.get('description')

            if category_name is not None and description is not None:
                if CategoryMaster.objects.filter(category_name=category_name).exists():
                    return Response("The category is already registered", status=status.HTTP_405_METHOD_NOT_ALLOWED)
                else:
                    CategoryMaster.objects.create(category_name=category_name, description=description)
                    return Response("The category is successfully created", status=status.HTTP_201_CREATED)
            else:
                return Response("The category name and description are needed", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None,id=None):
        try:
            if id is None :
                categoryobj=CategoryMaster.objects.all()
                serializerobj=CategoryMasterSerializer(categoryobj, many=True)
                return Response(serializerobj.data)
            else :
                if CategoryMaster.objects.filter(id=id):
                    categoryobj=CategoryMaster.objects.get(id=id)
                    serializerobj=CategoryMasterSerializer(categoryobj).data
                    return Response(serializerobj)
                else:
                    return Response("Category Id Not Match",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, format=None,id=None):
        try:
            if id is not None:
                if CategoryMaster.objects.filter(id=id):
                    categoryobj=CategoryMaster.objects.get(id=id)
                    categoryobj.delete()
                    return Response("Category deleted")
                else:
                    return Response("Category Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else :
                return Response("id is not valid",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, format=None,id=None):
        try:
            if id is not None:
                if CategoryMaster.objects.filter(id=id):
                    categoryobj= CategoryMaster.objects.get(id=id)
                    vars=request.data
                    category_name=vars.get('category_name')
                    description=vars.get('description')

                    if category_name !=None :
                        object=CategoryMaster.objects.filter(category_name=category_name).exists()
                        if object is False:
                            categoryobj.category_name=category_name
                        else:
                            pass

                    if description != None :
                        categoryobj.description=description

                    categoryobj.save()
                    return Response("Category is successfully updated") 
                else:
                    return Response("Category Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Category Detail Not Found enter ID",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubCategoryMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            vars = request.data
            categoryid=vars.get('categoryid')
            subcategory_name=vars.get('subcategory_name')
            description=vars.get('description')

            if categoryid != None and subcategory_name != None and description != None:
                if CategoryMaster.objects.filter(id=categoryid).exists():
                    if SubCategoryMaster.objects.filter(subcategory_name=subcategory_name).exists():
                        return Response("The Sub Category is already registered",)
                    else:
                        categoryobj=CategoryMaster.objects.get(id=categoryid)
                        SubCategoryMaster.objects.create(category=categoryobj,subcategory_name=subcategory_name,description=description)
                        return Response("The Sub Category is successfully",status=status.HTTP_201_CREATED)
                else:
                    return Response("Category Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("The categoryid name, subcategory and description is needed",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, format=None,id=None):
        try:
            if id is None :
                subcategoryobj=SubCategoryMaster.objects.all()
                mypagination = MyPagination()
                paginated_queryset = mypagination.paginate_queryset(subcategoryobj, request)
                serializerobj=SubcategoryMasterSerializer(paginated_queryset, many=True)
                return Response(serializerobj.data)
            else :
                if SubCategoryMaster.objects.filter(id=id):
                    subcategoryobj=SubCategoryMaster.objects.get(id=id)
                    serializerobj=SubcategoryMasterSerializer(subcategoryobj).data
                    return Response(serializerobj)
                else:
                    return Response("Subcategory Id Not Match",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, format=None,id=None):
        try:
            if id is not None:
                if SubCategoryMaster.objects.filter(id=id):
                    subcategoryobj= SubCategoryMaster.objects.get(id=id)
                    vars=request.data
                    subcategory_name=vars.get('subcategory_name')
                    description=vars.get('description')

                    if subcategory_name !=None :
                        object=SubCategoryMaster.objects.filter(subcategory_name=subcategory_name).exists()
                        if object is False:
                            subcategoryobj.subcategory_name=subcategory_name
                        else:
                            pass

                    if description != None :
                        subcategoryobj.description=description

                    subcategoryobj.save()
                    return Response("SubCategory is successfully updated") 
                else:
                    return Response("SubCategory Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Sub Category Detail Not Found enter ID",status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, format=None,id=None):
        try:
            if id is not None:
                if SubCategoryMaster.objects.filter(id=id):
                    subcategoryobj=SubCategoryMaster.objects.get(id=id).delete()
                    return Response("Sub Category is deleted successfully")

                else:
                    return Response("Sub Category Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else :
                return Response("id is not valid",status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductMasterAPI(APIView):

    def post(self, request, format=None):
        try:
            subcategoryid=request.POST.get('subcategoryid')
            product_name=request.POST.get('product_name')
            description=request.POST.get('description')
            price=request.POST.get('price')
            stock_quantity=request.POST.get('stock_quantity')
            main_image=request.FILES.get('main_image')


            if subcategoryid != None and product_name != None and description != None and price != None and stock_quantity != None and main_image!=None:
                if SubCategoryMaster.objects.filter(id=subcategoryid).exists():
                    subcatobj=SubCategoryMaster.objects.get(id=subcategoryid)
                    
                    if ProductMaster.objects.filter(product_name=product_name).exists():
                        return Response("Product is already registered")
                    else:
                        ProductMaster.objects.create(subcategory=subcatobj,product_name=product_name,description=description,price=price,stock_quantity=stock_quantity,main_image=main_image)
                        return Response("Product is successfully",status=status.HTTP_201_CREATED)
                   
                else:
                    return Response("Sub Category Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("The categoryid name, subcategoryid , product name,description,price,stock_quantity is needed",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def get(self, request, format=None, id=None):
        try:
            if id is None:
                product_objects = ProductMaster.objects.all()
                my_pagination = MyPagination()
                paginated_queryset = my_pagination.paginate_queryset(product_objects, request)
                serializer_objects = ProductMasterSerializer(paginated_queryset, many=True)
                return Response(serializer_objects.data)
            else:
                try:
                    product_obj = ProductMaster.objects.get(id=id)
                    product_serializer = ProductMasterSerializer(product_obj)
                    images = ProductImageMaster.objects.filter(product=product_obj)
                    reviews = ReviewProductMaster.objects.filter(product=product_obj)
                    image_serializer = ProductImageMasterSerializer(images, many=True)
                    review_serializer = ReviewProductMasterSerializer(reviews, many=True)

                    response_data = {
                        "product": product_serializer.data,
                        "images": image_serializer.data,
                        "reviews": review_serializer.data
                    }

                    return Response(response_data)
                except ProductMaster.DoesNotExist:
                    return Response("Product Id Not Found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, format=None,id=None):
        try:
            if id is not None:
                if ProductMaster.objects.filter(id=id):
                    productobj= ProductMaster.objects.get(id=id)
                    
                    subcategoryid=request.POST.get('subcategoryid')
                    product_name=request.POST.get('product_name')
                    description=request.POST.get('description')
                    price=request.POST.get('price')
                    stock_quantity=request.POST.get('stock_quantity')
                    main_image=request.FILES.get('main_image')

                    if product_name !=None :
                        if ProductMaster.objects.filter(product_name=product_name).exists():
                            pass
                        else:
                            productobj.product_name=product_name
                    
                    if description != None :
                        productobj.description=description

                    if price != None :
                        productobj.price=price

                    if stock_quantity != None :
                        productobj.stock_quantity=stock_quantity
                        
                    if main_image != None :
                        productobj.main_image=main_image


                    productobj.save()
                    return Response("Product is successfully updated") 
                else:
                    return Response("Product Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Product Detail Not Found enter ID",status=status.HTTP_400_BAD_REQUEST)
        

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
              
    def delete(self, request, format=None,id=None):
        try:
            if id is not None:
                if ProductMaster.objects.filter(id=id):
                    productobj=ProductMaster.objects.get(id=id).delete()
                    return Response("Product is successfully deleted")
                else:
                    return Response("Product Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else :
                return Response("id is not valid",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ReviewProductMasterAPI(APIView):
    
    def post(self, request, format=None):
        try:
            vars = request.data
            productid=vars.get('productid')
            rating=vars.get('rating')
            comment=vars.get('comment')
            created_at=vars.get('created_at')
            
            if productid != None and rating != None and comment != None :
                if ProductMaster.objects.filter(id=productid).exists():
                    if rating > 0 and rating<= 5:
                        projectobj=ProductMaster.objects.get(id=productid)                                
                        ReviewProductMaster.objects.create(product=projectobj,rating=rating,comment=comment,created_at=created_at)
                        return Response("Product review is successfully",status=status.HTTP_201_CREATED)
                    else:
                        return Response("Give rating 0-5 ",status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response("Product Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("The productid , rating , comment, created_at is needed",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    def delete(self, request, format=None,id=None):
        try:
            if id is not None:
                if ReviewProductMaster.objects.filter(id=id):
                    reviewobj=ReviewProductMaster.objects.get(id=id).delete()
                    return Response("Delete product successfully")
                else:
                    return Response("Review Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else :
                return Response("id is not valid",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, format=None,id=None):
        try:
            if id is not None:
                if ReviewProductMaster.objects.filter(id=id):
                    reviewobj= ReviewProductMaster.objects.get(id=id)
                    vars=request.data
                    rating=vars.get('rating')
                    comment=vars.get('comment')
                    created_at=vars.get('created_at')

                    if rating != None :
                        if rating > 0 and rating<= 5:
                            reviewobj.rating=rating

                    if comment != None :
                        reviewobj.comment=comment
                    
                    reviewobj.save()
                    return Response("Review is successfully updated") 
                else:
                    return Response("Review Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Review Detail Not Found enter ID",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request,formats=None,id=None):
        try:
            if id is None :
                reviewproductobj=ReviewProductMaster.objects.all()
                mypagination = MyPagination()
                paginated_queryset = mypagination.paginate_queryset(reviewproductobj, request)
                serializerobj=ReviewProductMasterSerializer(paginated_queryset, many=True)
                return Response(serializerobj.data)
            else:
                if ReviewProductMaster.objects.filter(id=id):
                    reviewproductobj=ReviewProductMaster.objects.get(id=id)
                    serializerobj=ReviewProductMasterSerializer(reviewproductobj).data
                    return Response(serializerobj)
                else:
                    return Response("Review Id Not Match",status=status.HTTP_400_BAD_REQUEST) 

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ProductImageMasterAPI(APIView):
    
    def post(self, request,fomate=None):
        try:
            productid=request.POST.get('productid')
            product_image=request.FILES.get('product_image')

            if productid != None and product_image!=None :
                if ProductMaster.objects.filter(id=productid).exists():
                    productobj=ProductMaster.objects.get(id=productid)
                    ProductImageMaster.objects.create(product=productobj, product_image=product_image)
                    return Response("Image created successfully",status=status.HTTP_201_CREATED)
                else :
                    return Response("Product Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else :
                return Response("The productid , product image is needed",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, format=None,id=None):
        try:
            if id is not None:
                if ProductImageMaster.objects.filter(id=id):
                    productimgobj=ProductImageMaster.objects.get(id=id).delete()
                    return Response("Image deleted successfully")
                else:
                    return Response("Review Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else :
                return Response("id is not valid",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
    def put(self, request, format=None,id=None):
        try:
            if id is not None:
                if ProductImageMaster.objects.filter(id=id):
                    productimgobj= ProductImageMaster.objects.get(id=id)
                    productid=request.POST.get('productid')
                    product_image=request.FILES.get('product_image')

                    if product_image != None :
                        productimgobj.product_image=product_image

                    productimgobj.save()
                    return Response("Image is successfully updated") 
                else:
                    return Response("productimage Id Not Match",status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Product Image Detail Not Found enter ID",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, format=None,id=None):
        try:
            if id is None :
                productimgobj=ProductImageMaster.objects.all()
                mypagination = MyPagination()
                paginated_queryset = mypagination.paginate_queryset(productimgobj, request)
                serializerobj=ProductImageMasterSerializer(paginated_queryset, many=True)
                return Response(serializerobj.data)
            else :
                if ProductImageMaster.objects.filter(id=id):
                    productobj=ProductImageMaster.objects.get(id=id)
                    serializerobj=ProductImageMasterSerializer(productobj).data
                    return Response(serializerobj)
                else:
                    return Response("Product Id Not Match",status=status.HTTP_400_BAD_REQUEST) 

        except Exception as e:
            return Response("An unexpected error occurred", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
