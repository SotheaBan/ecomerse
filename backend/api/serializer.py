from rest_framework import serializers
from .models import User_core

class UserCoreSerializer(serializers.ModelSerializer):
    class Meta: 
        model= User_core
        fields = '__all__'


class UserInputSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = User_core
        fields = ['email','password']