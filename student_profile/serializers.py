from rest_framework import serializers
from .models import *


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ('id', 'date', 'mark', 'user', 'subject')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'First_Name', 'Last_Name', 'subject')


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('id', 'subject_name',)
