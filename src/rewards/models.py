from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from quests.models import Quest

# Create your models here.

class Rewards(models.Model):

    type_choices = (
        ("exp", "exp"),
        ("weapon", "weapon"),
        ("armor", "armor"),
        ("potion", "potion"),
        ("bpoint", "bpoint"),
        ("scroll","scroll"),
        ("coin","coin"),
        ("other","other")
    )
    
    name = models.CharField(_("name"), max_length=64)
    quests = models.ForeignKey(Quest, on_delete=models.CASCADE, default=1)
    count = models.PositiveBigIntegerField(_("count"), default=0)
    upgrade_level = models.PositiveSmallIntegerField(_("upgrade_level"), null=True)
    reward_type = models.CharField(_("reward_type"), max_length=16, default="", choices=type_choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
