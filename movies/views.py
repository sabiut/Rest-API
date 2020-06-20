from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from .models import *


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = RatingSerializer

