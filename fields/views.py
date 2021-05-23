from django.http import HttpResponse
from django.template import loader

from .models import Laboratory


def index(request):
    laboratories = Laboratory.objects.all()
    template = loader.get_template('fields/index.html')
    context = {
        'laboratories': laboratories
    }
    return HttpResponse(template.render(context, request))
