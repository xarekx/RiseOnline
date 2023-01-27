from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Skill(models.Model):
    
    CLASSES = (
        ("Warrior", "Warrior"),
        ("Rogue", "Rogue"),
        ("Mage", "Mage"),
        ("Priest", "Priest")
    )
     
    skill_tree_choices = [('Train','Trainee'),
                          ('Asass','Assasin'),
                          ('Arch', 'Archer'),
                          ('Def','Defense'),
                          ('Mstr','Master'),
                          ('Buff', 'Buff'),
                          ('Heal','Heal'),
                          ('Dbf','Debuff'),
                          ('Fire', 'Fire'),
                          ('Ice','Ice'),
                          ('Light', 'Lighting'),
                          ('Attk','Attack'),]
    
    name = models.CharField(_("name"), max_length=64)
    skill_class = models.CharField(_("skill_class"), max_length=16, blank=True, null=True, choices=CLASSES)
    description = models.CharField(_("description"), max_length=128, null=True, blank=True)
    skill_tree = models.CharField(_("skill_tree"), max_length=32, default='', choices=skill_tree_choices)
    mana = models.SmallIntegerField(_("mana"), default=0)
    cooldown = models.FloatField(_("cooldown"), default=0)
    img = models.ImageField(_("img"), upload_to="media/skills/", null=True, blank=True)
    skill_point = models.SmallIntegerField(_("skill_point"), default=0)
    skill_level = models.SmallIntegerField(_("skill_level"), default=0)
    
    class Meta:
        db_table = "rise_skill"
        verbose_name = _("skill")
        verbose_name_plural = _('skills')
    
    
    def __str__(self):
        return str(self.skill_class)
    
    def save(self):
        super().save()
        image = Image.open(self.img.path)
        rgb_im = image.convert('RGB')
        if rgb_im.height !=44 or rgb_im.width!=44:
            output_size = (38, 38)
            rgb_im.thumbnail(output_size)
            rgb_im.save(self.img.path)
