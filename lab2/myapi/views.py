from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework import viewsets
from Home.models import Register
from .serializers import UserSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse

# Create your views here.

class Userlist(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = UserSerializers

@api_view(['GET','DELETE', 'PUT'])
def userUpadateOrDelete(requset , id):

    user = Register.objects.get(id=id)

    if(requset.method == 'GET'):
        response = UserSerializers(user)
        return JsonResponse(response.data)
    elif requset.method == "DELETE":
        user.delete()
        return HttpResponse("deleted user")
    elif requset.method == "PUT":
        data = JSONParser().parse(requset)
        serializer = UserSerializers(user, data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)





