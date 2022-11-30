from django.contrib import admin
from quests.models import Quests

@admin.register(Quests)
class Quests(admin.ModelAdmin):
    list_display = ['quest_name', 'quest_zone']

    list_filter = ['quest_zone']