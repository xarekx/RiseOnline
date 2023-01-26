from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(_("title"), max_length=64)
    article = models.TextField(_("article"))
    created_date = models.DateField(_("created_date"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="article_created_by", on_delete=models.CASCADE)
     
    class Meta:
        db_table = "rise_article"
        verbose_name = _("article")
        verbose_name_plural = _('articles')
         

    def __str__(self):
         return self.title