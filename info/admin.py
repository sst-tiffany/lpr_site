# Register your models here.

from django.contrib import admin

from .models import Information, UsefulLink

admin.site.register(Information)
admin.site.register(UsefulLink)
