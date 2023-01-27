from django.db import models
from zones.models import Zone
from django.utils.translation import gettext_lazy as _

class Monster(models.Model):
    name = models.CharField(_("name"), max_length=64, default="")
    level = models.PositiveSmallIntegerField(_("level"), default=1)
    zone_mob = models.ForeignKey(Zone, on_delete=models.CASCADE, default="")
    
    class Meta:
        db_table = "rise_monster"
        verbose_name = _("monster")
        verbose_name_plural = _('monsters')
    
    def __str__(self):
        return self.name
