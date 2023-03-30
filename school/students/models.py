from django.db import models
from django.db.models import Model


# Create your models here.


class Student (Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avg = models.FloatField()
    age = models.IntegerField()
