from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('movie', MovieViewSet)
router.register('rating', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
