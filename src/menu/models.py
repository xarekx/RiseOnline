from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class LeftSideMenu(models.Model):
    name = models.CharField(_("name"), max_length=32, null=True, blank=True)
    priority = models.IntegerField(_("priority"), unique=True, null=True, blank=True)

    def __str__(self):
        return self.name