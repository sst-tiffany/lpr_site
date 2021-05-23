#from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from .models import *

def index(request):
    infos = Information.objects.all()
    template = loader.get_template('index.html')
    context = {
        'info': infos
    }
    return HttpResponse(template.render(context, request))
