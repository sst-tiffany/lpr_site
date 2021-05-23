from django.db import models


class News(models.Model):
    date = models.DateField()
    text = models.TextField(max_length=10000)
