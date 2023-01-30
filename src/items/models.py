from email.policy import default
from random import choices
from django.db import models
from monsters.models import Monster
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    
    ITEM_TYPE_CHOICES = [('Sword','Sword'),
                          ('Dagger','Dagger'),
                          ('Bow', 'Bow'),
                          ('Axe','Axe'),
                          ('Spear','Spear'),
                          ('Staff', 'Staff'),
                          ('Mace','Mace'),
                          ('Warrior Armor','Warrior Armor'),
                          ('Mage Armor','Mage Armor'),
                          ('Rogue Armor','Rogue Armor'),
                          ('Priest Armor','Priest Armor'),
                          ('Accesories','Accesories'),]
    
    name = models.CharField(_("name"), max_length=64, null=True)
    img = models.ImageField(_("img"), upload_to="items/", null=True, blank=True)
    item_type = models.CharField(_("item_type"), max_length=32,  default="", choices=ITEM_TYPE_CHOICES)
    dropped_by = models.ForeignKey(Monster, on_delete=models.CASCADE, default="") 
    
    class Meta:
        db_table = "rise_item"
        verbose_name = _("item")
        verbose_name_plural = _('items')
    
    def __str__(self):
        return self.name 
