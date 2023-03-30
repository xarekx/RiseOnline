from django.shortcuts import render
from quests.models import Quest
from rewards.models import Reward
from django.core.paginator import Paginator

from menu.models import LeftSideMenu

# Create your views here.
def quests(request):
    
    left_side_item = LeftSideMenu.objects.all().order_by("priority")

    rewards = Reward.objects.all()
    
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    ordering = 'required_level'
    
    if direction == 'desc':
        ordering = '-{}'.format(ordering)
        
    if order_by is None or order_by == 'required_level':
        ordering = 'required_level'
        direction = 'asc'
    elif order_by  == 'quest_zone':
        ordering = 'quest_zone'  
    elif order_by  == 'quest_name':
        ordering = 'quest_name' 
    
    
        
    quest_list = Quest.objects.all().order_by(ordering)
    
    # pagination on the quest template
    paginator = Paginator(quest_list,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request, 'menu/quests.html', {'left_side_item': left_side_item,
                                                'rewards':rewards, 
                                                'direction':direction, 
                                                'quests': page_obj, 
                                                'order_by':order_by})
    
