from django.urls import path, include
from monsters.views import monsters

urlpatterns = [
    path('', monsters, name= "monsters")
]
