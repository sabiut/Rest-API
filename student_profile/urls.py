from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('marks', MarksViewSet)
router.register('teachers', TeachersViewSet)
router.register('subjects', SubjectsViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
