from django.db import models
from django.utils import timezone


class userModel(models.Model):
    user_name = models.CharField(max_length=32, unique=True, null=False)
    password = models.CharField(max_length=32, null=False, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class nationalCity(models.Model):
    provinceName = models.CharField(max_length=10)
    cityName = models.CharField(max_length=10)
    countyName = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    center = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    probe = models.CharField(max_length=3)
    silhouetteScore = models.FloatField()

    def __str__(self):
        return self.countyName


class traceRoute(models.Model):
    sourceIP = models.CharField(max_length=16)
    sourceCity = models.ForeignKey(nationalCity, on_delete=models.CASCADE)
    targetIP = models.CharField(max_length=16)
    TTL = models.IntegerField()
    time = models.FloatField()
    routers = models.CharField(max_length=1024)
    stability = models.CharField(max_length=50)
