from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()
    hours = models.CharField(max_length=100)
    books = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    research_field = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
