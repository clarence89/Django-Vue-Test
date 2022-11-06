from django.urls import path, include
""" from django.contrib.auth.models import User """
from rest_framework import routers
from django.contrib import admin
from restapi.views import  UserViewSet,AnimalViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'animals', AnimalViewSet)


urlpatterns = [
    path('models/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
