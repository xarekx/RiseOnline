from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import os.path
from config import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(_("title"), max_length=64)
    article = models.TextField(_("article"), max_length=256)
    full_article = models.TextField(_("full_article"), default="")
    created_date = models.DateField(_("created_date"), auto_now=True)
    created_by = models.ForeignKey(User, related_name="article_created_by", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "rise_article"
        verbose_name = _("article")
        verbose_name_plural = _('articles')
         
    def __str__(self):
         return self.title
     
    def replace_space_and_dot_in_title(self):
        temp_title = str.replace(self.title.lower(),".", "_")
        return str.replace(temp_title ," ", "_")
     
    def create_article_file(self):
        
        save_path = os.path.join(settings.BASE_DIR, 'templates/articles/'+ Article.replace_space_and_dot_in_title(self) + ".html")
        
        new_article = open(save_path, "w")
        
        new_article.write('''
{% extends 'base.html' %}
{% block title %} Rise Online World ''' + str(self.title) + ''' {% endblock %}

{% block body %}
        <div class="flex flex-col w-full">
            <div class="bg-[#191D21] text-[#dbae28] pl-4 pr-4 py-2 sm:px-6 md:pl-6">
                ''' + str(self.title) + ''' 
            </div>
            <div class="relative bg-[#191D21] text-white pl-3 pr-3 pt-2 border-t-[0.5px] border-white md:pl-8 lg:pr-10">
                ''' + str(self.full_article) + '''
            <div class="flex pt-10 xl:pt-16">
                    <div class="absolute bottom-3 right-6 
                    xl:bottom-5 text-2xs md:text-base" > ''' + str(self.created_by) + ' ' + str(self.created_date) + ''' </div>
                </div>
            </div>
        </div>
{% endblock %}''')
        new_article.close()
        
    
@receiver(post_save, sender=Article)
def create_article(sender, instance, created, **kwargs):
        Article.create_article_file(Article.objects.get(pk=instance.id))

        
