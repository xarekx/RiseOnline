from django.db import models
from zones.models import Zones
from django.utils.translation import gettext_lazy as _

class Quest(models.Model):
    quest_name = models.CharField(_("quest_name"), max_length=128, default="")
    required_level = models.PositiveIntegerField(_("required_level"), default=1)
    npc_name = models.CharField(_("npc_name"), max_length=64, default="")
    description = models.CharField(_("description"), max_length=128, default="")
    quest_zone = models.ForeignKey(Zones, on_delete=models.CASCADE, default="")
    
    class Meta:
        db_table = "rise_quest"
        verbose_name = _("quest")
        verbose_name_plural = _('quests')

    def __str__(self):
        return self.quest_name
