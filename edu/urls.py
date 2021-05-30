from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='edu'),
    path('courses/', views.courses, name='courses'),
    path('professors/', views.professors, name='professors'),
    path('students/', views.students, name='students'),
]
