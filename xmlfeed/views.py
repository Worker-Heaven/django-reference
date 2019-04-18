from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person, Site

def index(request):
    site_list = Site.objects.all()

    context = {
        'sites': site_list,
    }

    return render(request, 'xmlfeed/index.html', context)

def summary(request):
    members = Person.objects.order_by('name')

    template = loader.get_template('xmlfeed/summary.html')
    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))