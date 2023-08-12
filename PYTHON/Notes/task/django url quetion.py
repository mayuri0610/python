

# from django.shortcuts import render,redirect
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
# from rest_framework.permissions import IsAuthenticated

# import json
# from django.http import JsonResponse
# from django.core import serializers as core_serializers
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from django.contrib import auth
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User



# # from .serializer import *
# # from .models import *
# # from accounts.views import get_user_usertype_userprofile
# # from accounts.paginatorviews import MyPagination













l1 = [2, 5, 7, 9, 3, 5, 6, 3]
l2 = [8, 3, 4, 6, 10, 14, 24]
l3 = []

# Merge the two lists using only append

for num in l2:
    l1.append(num)

print("Merged list:", l1)

# Find unique elements
l3 = []
for num in l1:
    if num not in l3:
        l3.append(num)

print("Unique elements:", l3)


n = len(l3)
print(n)        # 11

for i in range(n - 1):      #    10       i= 0
    for j in range(0, n - i - 1):       # 0 (0,10)
        if l3[j] > l3[j + 1]:
            l3[j], l3[j + 1] = l3[j + 1], l3[j]



print("Sorted l3:", l3)










