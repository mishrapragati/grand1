from django.db import models
from datetime import datetime


class user(models.Model):
    name = models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.IntegerField()
    mobileno=models.IntegerField()


 class diet(models.Model):
        dietname = models.CharField(max_length=30)
        calindiet = models.IntegerField()
        protienindiet = models.IntegerField()
        fatindiet = models.IntegerField()


 class order(models.Model):
     dietorderbyuser=models.CharField(max_length=30)
     timestamp = 1545730073
     dt_object = datetime.fromtimestamp(timestamp)
     userwhoordered=models.CharField(max_length=30)
