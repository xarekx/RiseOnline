from django.urls import path, include
from items.views import items,weapons

urlpatterns = [
    path('', items, name='items'),
    path('weapons',weapons, name='weapons')
]
