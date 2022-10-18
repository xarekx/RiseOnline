from django.urls import include, path
from zones.views import zones, dorion, protean, haddar, haggar, narun_tower, death_valley, lunaskar

urlpatterns = [
    path('', zones, name="zones"),
    path('dorion', dorion, name="dorion"),
    path('protean', protean, name="protean"),
    path('lunaskar', lunaskar, name="lunaskar"),
    path('haggar', haggar, name="haggar"),
    path('haddar', haddar, name="haddar"),
    path('death_valley', death_valley, name="death_valley"),
    path('narun_tower', narun_tower, name="narun_tower"),
]
