from django.shortcuts import render
from menu.models import LeftSideMenu
from items.models import Item

# Create your views here.

def weapons(request):
    left_side_item = LeftSideMenu.objects.all().order_by("priority")
    swords = Item.objects.all().filter(item_type="Sword")
    axes = Item.objects.all().filter(item_type="Axe")
    daggers = Item.objects.all().filter(item_type="Dagger").distinct('name')
    spears = Item.objects.all().filter(item_type="Spear")
    staffs = Item.objects.all().filter(item_type="Staff")
    maces = Item.objects.all().filter(item_type="Mace")
    bows = Item.objects.all().filter(item_type="Bow")
    
    return render(request, 'items/weapons.html', { 'left_side_item': left_side_item, 
                                                  'swords':swords, 
                                                  'daggers':daggers, 
                                                  'axes':axes,
                                                  'spears':spears,
                                                  'staffs':staffs,
                                                  'maces':maces,
                                                  'bows':bows})

def armors(request):
    left_side_item = LeftSideMenu.objects.all()
    warrior_armors = Item.objects.all().filter(item_type="Warrior Armor")
    priest_armors = Item.objects.all().filter(item_type="Priest Armor")
    rogue_armors = Item.objects.all().filter(item_type="Rogue Armor")
    mage_armors = Item.objects.all().filter(item_type="Mage Armor")
    
    return render(request, 'items/armors.html', { 'left_side_item': left_side_item, 
                                                 'warrior_armors':warrior_armors,
                                                 'priest_armors':priest_armors,
                                                 'rogue_armors':rogue_armors,
                                                 'mage_armors':mage_armors})