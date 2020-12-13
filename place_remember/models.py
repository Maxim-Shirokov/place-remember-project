from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserLocation(models.Model):
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlocation')
    name = models.CharField(max_length=120)
    comment = models.TextField(null=True)
