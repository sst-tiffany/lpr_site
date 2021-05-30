from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()
    hours = models.CharField(max_length=100)
    books = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Professor(models.Model):
    full_name = models.CharField(max_length=200)
    research_field = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    year = models.IntegerField()
    advisor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
