from django.contrib import admin
from monsters.models import Monsters

# Register your models here.
@admin.register(Monsters)
class Monsters(admin.ModelAdmin):
    list_display =  ['name', 'level', 'zone_mob']