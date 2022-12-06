from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from quests.models import Quests

# Create your models here.

class Rewards(models.Model):

    name = models.CharField(_("name"), max_length=64)
    quest_id = models.ForeignKey(Quests, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
