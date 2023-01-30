from django.contrib import admin
from skills.models import Skill

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display = ['name', 'skill_class','skill_tree']

    list_filter = ['skill_class']
