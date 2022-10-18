from django.contrib import admin
from skills.models import Skills

@admin.register(Skills)
class Skills(admin.ModelAdmin):
    list_display = ['name', 'skill_class','skill_tree']

    list_filter = ['skill_class']
