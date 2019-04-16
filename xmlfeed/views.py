from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person

def index(request):
    members = Person.objects.order_by('name')

    template = loader.get_template('xmlfeed/index.html')
    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))

