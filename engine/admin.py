from django.contrib import admin
from .models import ResortInfo
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(ResortInfo)
