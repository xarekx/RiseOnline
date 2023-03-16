from django.shortcuts import render
from menu.models import LeftSideMenu

def contacts(request):
    
    left_side_item = LeftSideMenu.objects.all().order_by("priority")
    
    return render(request, 'menu/contacts.html', { 'left_side_item':left_side_item})
