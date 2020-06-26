from django.contrib.auth.models import User
from django.db import models


class Subjects(models.Model):
    subject_name = models.CharField(max_length=15)

    def __str__(self):
        return self.subject_name


class Teachers(models.Model):
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.First_Name


class Marks(models.Model):
    date = models.DateField()
    mark = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.Firts_name
