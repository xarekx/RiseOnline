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
    axes = Items.objects.all().filter(item_type="Axe")
    daggers = Items.objects.all().filter(item_type="Dagger").distinct('name')
    spears = Items.objects.all().filter(item_type="Spear")
    staffs = Items.objects.all().filter(item_type="Staff")
    maces = Items.objects.all().filter(item_type="Mace")
    bows = Items.objects.all().filter(item_type="Bow")
    
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
    warrior_armors = Items.objects.all().filter(item_type="Warrior Armor")
    priest_armors = Items.objects.all().filter(item_type="Priest Armor")
    rogue_armors = Items.objects.all().filter(item_type="Rogue Armor")
    mage_armors = Items.objects.all().filter(item_type="Mage Armor")
    
    return render(request, 'items/armors.html', { 'left_side_item': left_side_item, 
                                                 'warrior_armors':warrior_armors,
                                                 'priest_armors':priest_armors,
                                                 'rogue_armors':rogue_armors,
                                                 'mage_armors':mage_armors})