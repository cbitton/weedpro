from django.contrib import admin

from weeds.models import Weed

class WeedAdmin (admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']

admin.site.register(Weed, WeedAdmin)
