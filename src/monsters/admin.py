from django.contrib import admin
from monsters.models import Monster

# Register your models here.
@admin.register(Monster)
class Monster(admin.ModelAdmin):
    list_display =  ['name', 'level', 'zone_mob']