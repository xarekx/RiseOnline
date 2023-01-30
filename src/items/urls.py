from django.urls import path
from items.views import weapons,armors

urlpatterns = [
    path('weapons', weapons, name='weapons'),
    path('armors', armors, name='armors')
]
