from django.http import HttpResponse
from django.template import loader

from .models import Person, Course


def index(request):
    persons = Person.objects.all()
    courses = Course.objects.all()
    template = loader.get_template('persons_and_courses/index.html')
    context = {
        'persons': persons,
        'courses': courses
    }
    return HttpResponse(template.render(context, request))
