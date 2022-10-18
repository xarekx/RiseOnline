from django.shortcuts import render
from monsters.models import Monsters
from items.models import Items
from menu.models import LeftSideMenu

# Create your views here.
def monsters(request):
    left_side_item = LeftSideMenu.objects.all()
    monsters = Monsters.objects.all()
    items = Items.objects.values()
    
    return render(request, 'menu/monsters.html', {'left_side_item': left_side_item, "monsters":monsters, "items":items})