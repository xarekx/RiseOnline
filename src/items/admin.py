from django.contrib import admin
from items.models import Items

@admin.register(Items)
class Monsters(admin.ModelAdmin):
    list_display =  ['name',"dropped_by"]