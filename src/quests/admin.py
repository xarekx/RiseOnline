from django.contrib import admin
from quests.models import Quests

@admin.register(Quests)
class Quests(admin.ModelAdmin):
    list_display = ['title', 'start_zone']

    list_filter = ['start_zone']