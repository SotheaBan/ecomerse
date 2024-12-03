from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User_core
from .serializer import UserCoreSerializer,UserInputSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#Handle the user listing and input 
@api_view(['GET','POST'])
def user_listing(request): 
    if request.method == 'GET':
        queryset = User_core.objects.all()
        seriaizer = UserCoreSerializer(queryset, many=True)

        return Response(seriaizer.data)
    
    elif request.method == 'POST':
        seriaizer = UserCoreSerializer(data =request.data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response(seriaizer.data,status=status.HTTP_201_CREATED)
        return Response(seriaizer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def User_Login(request):
    password = request.data.get('password')
    email = request.data.get('email') 

    try : 
        if User_core.objects.filter(email=email):
            if User_core.objects.filter(password = password):
                 return Response ("User logined")
            else :
             return Response ("password Error")
        else :
            return Response ("password Error")

    except: 
        return Response("Error logic")