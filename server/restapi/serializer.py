from rest_framework import serializers
from .models import CustomUser, Animal
from django.db import models
from rest_framework import permissions
from rest_framework.decorators import  permission_classes
from django.contrib.auth.hashers import make_password




class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ['url','id','name']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['url', 'username','password', 'email', 'colour', 'animals','tiger_type']
    def validate_password(self, value):
        return make_password(value)
