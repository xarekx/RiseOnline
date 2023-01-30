from django.contrib import admin
from items.models import Item

@admin.register(Item)
class Monsters(admin.ModelAdmin):
    list_display =  ['name',"dropped_by"]