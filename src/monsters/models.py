from django.db import models
from zones.models import Zones
from django.utils.translation import gettext_lazy as _

class Monsters(models.Model):
    name = models.CharField(_("name"), max_length=64, default="")
    level = models.PositiveSmallIntegerField(_("level"), default=1)
    zone_mob = models.ForeignKey(Zones, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return self.name
