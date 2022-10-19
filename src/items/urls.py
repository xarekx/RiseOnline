from django.urls import path, include
from items.views import items,weapons,armors

urlpatterns = [
    path('', items, name='items'),
    path('weapons', weapons, name='weapons'),
    path('armors', armors, name='armors')
]
