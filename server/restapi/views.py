from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Animal
from .serializer import  UserSerializer, AnimalSerializer
from rest_framework import permissions, status
from rest_framework.decorators import action, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['update','partial_update','destroy','list']:
            self.permission_classes = [permissions.DjangoModelPermissions,]
        elif self.action in ['create']:
            self.permission_classes = [permissions.AllowAny,]
        return super(self.__class__, self).get_permissions()


    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


    @action(detail=False, methods=["post"],permission_classes=[permissions.AllowAny])
    def authenticate(self ,request):
        customer = self.get_queryset().filter(username=request.POST["username"], password = request.POST["password"])
        serializer = self.get_serializer(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



"""     @action(detail=False, methods=["post"],permission_classes=[permissions.AllowAny])
    def register_users(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            CustomUser.objects.create_user(
                serialized.init_data['email'],
                serialized.init_data['username'],
                serialized.init_data['password']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST) """


class AnimalViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['update','partial_update','destroy','create']:
            self.permission_classes = [permissions.DjangoModelPermissions,]
        elif self.action in ['list']:
            self.permission_classes = [permissions.AllowAny,]
        return super(self.__class__, self).get_permissions()
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
