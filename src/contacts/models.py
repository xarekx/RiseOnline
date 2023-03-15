from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Contact(models.Model):
    
    MSG_TYPE_CHOICES = [('Items', 'Items'),
                          ('Monsters','Monsters'),
                          ('Drops', 'Drops'),
                          ('Rewards','Rewards'),
                          ('Quests','Quests'),
                          ('News', 'News'),
                          ('Other','Other')]
    
    msg_title = models.CharField(_("msg_title"), max_length=64, null=False)
    msg_type = models.CharField(_("msg_type"), choices=MSG_TYPE_CHOICES, max_length=16, default=MSG_TYPE_CHOICES[0])
    msg_description = models.CharField(_("msg_description"), max_length=500, null=False)
    
    class Meta:
        db_table = "rise_contact"
        verbose_name = _("contact")
        verbose_name_plural = _('contacts')
    
    def __str__(self):
        return self.name 