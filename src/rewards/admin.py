from django.contrib import admin
from .models import Reward

@admin.register(Reward)
class Reward(admin.ModelAdmin):
    list_display = ['quests', 'name']


