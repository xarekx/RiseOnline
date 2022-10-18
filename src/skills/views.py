from django.shortcuts import render
from skills.models import Skills
from menu.models import LeftSideMenu

# Create your views here.
skills_all = Skills.objects.all()
left_side_item = LeftSideMenu.objects.all()

def warrior(request):
    warrior_attack = skills_all.filter(skill_class = "Warrior", skill_tree = 'Attk').order_by('skill_point')
    warrior_defense = skills_all.filter(skill_class = "Warrior", skill_tree = 'Def').order_by('skill_point')
    warrior_master = skills_all.filter(skill_class = "Warrior", skill_tree = 'Mstr').order_by('skill_point')
    warrior_trainee = skills_all.filter(skill_class = "Warrior" ,skill_tree = 'Train').order_by('skill_point')
     
    return render(request, 'skills/warrior.html', {'left_side_item': left_side_item, 
                                                # 'warrior': warrior,
                                                'warrior_attack': warrior_attack, 
                                                'warrior_defense': warrior_defense,
                                                'warrior_master':warrior_master,
                                                'warrior_trainee':warrior_trainee 
                                                })

def priest(request):
    priest_buff = skills_all.filter(skill_class = 'Priest', skill_tree = 'Buff').order_by('skill_point')
    priest_heal = skills_all.filter(skill_class = 'Priest', skill_tree = 'Heal').order_by('skill_point')
    priest_debuff = skills_all.filter(skill_class = 'Priest', skill_tree = 'Dbf').order_by('skill_point')
    priest_master = skills_all.filter(skill_class = 'Priest', skill_tree = 'Mstr').order_by('skill_point')
    priest_trainee = skills_all.filter(skill_class = 'Priest', skill_tree = 'Train').order_by('skill_point')
     
    return render(request, 'skills/priest.html', {'left_side_item': left_side_item, 
                                                'priest_buff': priest_buff,
                                                'priest_heal': priest_heal,
                                                'priest_debuff' : priest_debuff,
                                                'priest_master' : priest_master,
                                                'priest_trainee' : priest_trainee
                                                })

def rogue(request):
    
    rogue_assas = skills_all.filter(skill_class = 'Rogue', skill_tree = 'Asass').order_by('skill_point')
    rogue_arch = skills_all.filter(skill_class = 'Rogue', skill_tree = 'Arch').order_by('skill_point')
    rogue_scout = skills_all.filter(skill_class = 'Rogue', skill_tree = 'Def').order_by('skill_point')
    rogue_master = skills_all.filter(skill_class = 'Rogue', skill_tree = 'Mstr').order_by('skill_point')
    rogue_trainee = skills_all.filter(skill_class = 'Rogue', skill_tree = 'Train').order_by('skill_point')
     
    return render(request, 'skills/rogue.html', {'left_side_item': left_side_item, 
                                                'rogue_assas': rogue_assas,
                                                'rogue_arch': rogue_arch,
                                                'rogue_scout' : rogue_scout,
                                                'rogue_master' : rogue_master,
                                                'rogue_trainee' : rogue_trainee
                                                })

def mage(request):
    mage_fire = skills_all.filter(skill_class = 'Mage', skill_tree = 'Fire').order_by('skill_point')
    mage_ice = skills_all.filter(skill_class = 'Mage', skill_tree = 'Ice').order_by('skill_point')
    mage_light = skills_all.filter(skill_class = 'Mage', skill_tree = 'Light').order_by('skill_point')
    mage_master = skills_all.filter(skill_class = 'Mage', skill_tree = 'Mstr').order_by('skill_point')
    mage_trainee = skills_all.filter(skill_class = 'Mage', skill_tree = 'Train').order_by('skill_point')
     
    return render(request, 'skills/mage.html', {'left_side_item': left_side_item, 
                                                'mage_fire': mage_fire,
                                                'mage_ice': mage_ice,
                                                'mage_light' : mage_light,
                                                'mage_master' : mage_master,
                                                'mage_trainee' : mage_trainee
                                                })