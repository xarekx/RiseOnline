from django.urls import path, include
from quests.views import quests

urlpatterns = [
    path('', quests, name="quests")
]
