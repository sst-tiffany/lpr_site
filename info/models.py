# Create your models here.

from django.db import models


class Information(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=10000)
