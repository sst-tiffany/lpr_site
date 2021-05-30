from django.contrib import admin

from .models import Course, Professor, Student

admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Student)
