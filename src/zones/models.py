from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Zone(models.Model):
    name = models.CharField(_("name"), max_length=64)
    required_level = models.PositiveSmallIntegerField(_("required_level"), default=1)
    img = models.ImageField(_("img"), upload_to="zones/", null=True, blank=True)
    
    class Meta:
        db_table = "rise_zone"
        verbose_name = _("zone")
        verbose_name_plural = _('zones')
    
    def __str__(self):
        return self.name
       
    def save(self):
        super().save()
        image = Image.open(self.img.path)
        rgb_im = image.convert('RGB')
        if rgb_im.height !=185 or rgb_im.width!=387:
            output_size = (387, 185)
            rgb_im.thumbnail(output_size)
            rgb_im.save(self.img.path)
