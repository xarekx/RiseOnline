from django.urls import path, include
from skills.views import mage, warrior, rogue, priest


urlpatterns = [
    path('warrior', warrior, name='warrior'),
    path('mage', mage, name='mage'),
    path('rogue', rogue, name='rogue'),
    path('priest', priest, name='priest')
]
