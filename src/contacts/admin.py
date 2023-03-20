from django.contrib import admin
from contacts.models import Contact

# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    
    list_display = ['msg_title', 'msg_type', 'msg_description','msg_read']
    
    list_filter = ['msg_type','msg_read']
