from django.contrib import admin

from .models import Person, Site

admin.site.register(Person)
admin.site.register(Site)
