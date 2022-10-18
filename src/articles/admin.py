from django.contrib import admin
from articles.models import Article

@admin.register(Article)
class Article(admin.ModelAdmin):
    pass
