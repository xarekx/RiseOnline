from django.shortcuts import render
from menu.models import LeftSideMenu
from items.models import Items

# Create your views here.
def items(request):
    left_side_item = LeftSideMenu.objects.all()
    
    return render(request, 'menu/items.html', { 'left_side_item': left_side_item})


def weapons(request):
    left_side_item = LeftSideMenu.objects.all()
    swords = Items.objects.all().filter(item_type="Sword")
    
    return render(request, 'items/weapons.html', { 'left_side_item': left_side_item, 'swords':swords})

def armors(request):
    left_side_item = LeftSideMenu.objects.all()
    
    return render(request, 'items/armors.html', { 'left_side_item': left_side_item})