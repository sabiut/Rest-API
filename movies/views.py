from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    Add WSGIPassAuthorization On on the apache2.conf file
    if you are serving your site on a apache server. 
    Otherwise you won't be able to authenticate
    """




class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rate = Rating.objects.get(user=user.id, movie=movie.id)
                rate.stars = stars
                rate.save()
                serialize = RatingSerializer(rate, many=False)
                response = {'success_message': 'you have updated your rating', 'result': serialize.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rate = Rating.objects.create(user=user, movie=movie, stars=stars)
                serialize = RatingSerializer(rate, many=False)
                response = {'success_message': 'successfully rated', 'result': serialize.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'error_message': 'please rate the video'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'error_message': 'You are not allow to update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'error_message': 'You are not allow to create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
