from django.http import HttpResponse
from django.template import loader

from .models import Course, Professor, Student


def index(request):
    template = loader.get_template('edu/index.html')
    return HttpResponse(template.render({}, request))


def courses(request):
    courses = Course.objects.order_by('semester', 'name').all()
    template = loader.get_template('edu/courses.html')
    context = {
        'courses': courses
    }
    return HttpResponse(template.render(context, request))


def professors(request):
    professors = Professor.objects.order_by('full_name').all()
    template = loader.get_template('edu/professors.html')
    context = {
        'professors': professors
    }
    return HttpResponse(template.render(context, request))


def students(request):
    students = Student.objects.order_by('year', 'full_name').all()
    template = loader.get_template('edu/students.html')
    context = {
        'students': students
    }
    return HttpResponse(template.render(context, request))
