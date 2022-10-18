from django.db import models
from django.utils.translation import gettext_lazy as _

class Quests(models.Model):
    title = models.CharField(_("title"), max_length=128)
    required_level = models.PositiveIntegerField(_("required_level"), default=1)
    start_zone = models.CharField(_("start_zone"), max_length=64)
    exp = models.IntegerField(_("exp"), default=0)

    def __str__(self):
        return self.title
