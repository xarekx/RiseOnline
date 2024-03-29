from django.contrib import admin
from quests.models import Quest

@admin.register(Quest)
class Quest(admin.ModelAdmin):
    list_display = ['quest_name', 'quest_zone', 'required_level']

    list_filter = ['quest_zone']