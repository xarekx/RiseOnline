from django.shortcuts import render
from quests.models import Quest
from rewards.models import Reward
from django.core.paginator import Paginator

from menu.models import LeftSideMenu

# Create your views here.
def quests(request):
    quest_list = Quest.objects.all().order_by('required_level')
    left_side_item = LeftSideMenu.objects.all().order_by("priority")
    rewards = Reward.objects.all()
    # pagination on the quest template
    # paginator = Paginator(quest_list,25)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    return render(request, 'menu/quests.html', {'left_side_item': left_side_item
                                                , 'quests': quest_list, 'rewards':rewards})
    
