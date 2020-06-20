from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import *


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            # user = request.user
            user = User.objects.get(id=1)

            try:
                rate = Rating.objects.get(user=user.id, movie=movie.id)
                rate.stars = stars
                rate.save()
                serialize = RatingSerializer(rate, many=False)
                response = {'success_message': 'you have updated your rating', 'result': serialize.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rate= Rating.objects.create(user=user, movie=movie, stars=stars)
                serialize = RatingSerializer(rate, many=False)
                response = {'success_message': 'successfully rated', 'result': serialize.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'error_message': 'please rate the video'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
