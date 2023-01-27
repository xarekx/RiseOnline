from django.shortcuts import render
from quests.models import Quest
from rewards.models import Rewards

from menu.models import LeftSideMenu

# Create your views here.
def quests(request):
    quest_list = Quest.objects.all().order_by('required_level')
    left_side_item = LeftSideMenu.objects.all()
    rewards = Rewards.objects.all()
    
    return render(request, 'menu/quests.html', {'left_side_item': left_side_item
                                                , 'quests': quest_list, 'rewards':rewards})
    