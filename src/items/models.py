from email.policy import default
from random import choices
from django.db import models
from monsters.models import Monsters
from django.utils.translation import gettext_lazy as _

class Items(models.Model):
    
    ITEM_TYPE_CHOICES = [('Sword','Sword'),
                          ('Dagger','Dagger'),
                          ('Bow', 'Bow'),
                          ('Axe','Axe'),
                          ('Spear','Spear'),
                          ('Staff', 'Staff'),
                          ('Mace','Mace'),
                          ('Warrior Armor','Warrior_armor'),
                          ('Mage Armor','Mage_armor'),
                          ('Rogue Armor','Rogue_armor'),
                          ('Priest Armor','Priest_armor'),
                          ('Accesories','Accesories'),]
    
    name = models.CharField(_("name"), max_length=64, null=True)
    img = models.ImageField(_("img"), upload_to="items/", null=True, blank=True)
    item_type = models.CharField(_("item_type"), max_length=32,  default="", choices=ITEM_TYPE_CHOICES)
    dropped_by = models.ForeignKey(Monsters, on_delete=models.CASCADE, default="") 
    
    def __str__(self):
        return self.name 
