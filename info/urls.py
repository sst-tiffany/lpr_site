from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('js/bootstrap.min.js HTTP/1.1', views.index, name='index'),
]
