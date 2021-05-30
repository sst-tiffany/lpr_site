from django.db import models


class News(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=300)
    text = models.TextField(max_length=10000)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name
