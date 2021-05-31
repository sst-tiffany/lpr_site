from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    information = Information.objects.all()
    links = UsefulLink.objects.all()
    template = loader.get_template('info/index.html')
    context = {
        'information': information,
        'links': links
    }
    return HttpResponse(template.render(context, request))
