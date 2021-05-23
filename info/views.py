from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    information = Information.objects.all()[0]
    template = loader.get_template('info/index.html')
    context = {
        'title': information.title,
        'info': information.info
    }
    return HttpResponse(template.render(context, request))
