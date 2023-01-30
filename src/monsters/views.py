from django.shortcuts import render
from monsters.models import Monster
from items.models import Item
from menu.models import LeftSideMenu

# Create your views here.
def monsters(request):
    left_side_item = LeftSideMenu.objects.all()
    monsters = Monster.objects.all()
    items = Item.objects.values()
    
    return render(request, 'menu/monsters.html', {'left_side_item': left_side_item, "monsters":monsters, "items":items})