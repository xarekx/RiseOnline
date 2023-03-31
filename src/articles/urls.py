from django.urls import path,re_path
from articles.views import articles

urlpatterns = [
    re_path(r'^patch_notes_[0-9]_[0-9]_[0-9]$', articles, name='articles')
]
