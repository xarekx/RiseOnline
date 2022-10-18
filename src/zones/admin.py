from django.contrib import admin
from zones.models import Zones

@admin.register(Zones)
class Zones(admin.ModelAdmin):
    list_display =  ['name', 'required_level']
