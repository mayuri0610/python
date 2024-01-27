from rest_framework import status

def success(self, msg):
    response = {
        "data":msg,
        "status" : "success",
        "code"   : status.HTTP_200_OK
    }
    return response

def error(self, msg):
    response = {
        "data":msg,
        "status" :"failed",
        "code"   : status.HTTP_400_BAD_REQUEST
    }
    return response