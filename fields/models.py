from django.db import models


class Laboratory(models.Model):
    category = models.CharField(max_length=255)
    head = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
