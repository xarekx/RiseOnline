from django.contrib import admin
from zones.models import Zone

@admin.register(Zone)
class Zone(admin.ModelAdmin):
    list_display =  ['name', 'required_level']
