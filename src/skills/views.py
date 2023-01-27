from django.shortcuts import render
from skills.models import Skill
from menu.models import LeftSideMenu
from django.template import loader
from django.http import HttpResponse

# Create your views here.
skills_all = Skill.objects.all()
left_side_item = LeftSideMenu.objects.all()

def count_class_skill_type(class_name):
    
    class_skill_type = list(skills_all.filter(skill_class=class_name).values_list('skill_tree',flat=True).distinct())
    return class_skill_type

def get_skills(class_name, skills_tree):
    skills = skills_all.filter(skill_class = class_name, skill_tree = skills_tree).order_by('skill_point')
    return skills

def warrior(request):
   
    return render(request, 'skills/warrior.html', {'left_side_item': left_side_item, 
                                                'warrior_attack': get_skills('Warrior', 'Attk'),
                                                'warrior_defense': get_skills('Warrior', 'Def'),
                                                'warrior_master':get_skills('Warrior', 'Mstr'),
                                                'warrior_trainee':get_skills('Warrior', 'Train'),
                                                'count_class_skill_type':count_class_skill_type('Warrior')
                                                })

def priest(request):
     
    return render(request, 'skills/priest.html', {'left_side_item': left_side_item, 
                                                'priest_buff': get_skills('Priest','Buff'),
                                                'priest_heal': get_skills('Priest','Heal'),
                                                'priest_debuff' : get_skills('Priest','Dbf'),
                                                'priest_master' : get_skills('Priest','Mstr'),
                                                'priest_trainee' : get_skills('Priest','Train'),
                                                'count_class_skill_type':count_class_skill_type('Priest')
                                                })
    


def rogue(request):
   
    return render(request, 'skills/rogue.html', {'left_side_item': left_side_item, 
                                                'rogue_assas': get_skills('Rogue', 'Asass'),
                                                'rogue_arch': get_skills('Rogue', 'Arch'),
                                                'rogue_scout' : get_skills('Rogue', 'Def'),
                                                'rogue_master' : get_skills('Rogue', 'Mstr'),
                                                'rogue_trainee' : get_skills('Rogue', 'Train'),
                                                'count_class_skill_type': count_class_skill_type('Rogue')
                                                })

def mage(request):
     
    return render(request, 'skills/mage.html', {'left_side_item': left_side_item, 
                                                'mage_fire': get_skills('Mage','Fire'),
                                                'mage_ice': get_skills('Mage','Ice'),
                                                'mage_light' : get_skills('Mage','Light'),
                                                'mage_master' : get_skills('Mage','Mstr'),
                                                'mage_trainee' : get_skills('Mage','Train'),
                                                'count_class_skill_type': count_class_skill_type('Mage')
                                                })