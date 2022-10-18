from django.contrib import admin
from menu.models import LeftSideMenu

# Register your models here.
@admin.register(LeftSideMenu)
class LefSideMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority']