from django.contrib import admin
from items.models import Item

@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display =  ['name',"dropped_by"]
    
    list_filter = ['item_type']