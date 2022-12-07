from django.contrib import admin
from .models import Rewards

@admin.register(Rewards)
class Rewards(admin.ModelAdmin):
    list_display = ['quests']

