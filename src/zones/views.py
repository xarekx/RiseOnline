from django.shortcuts import render
from menu.models import LeftSideMenu
from zones.models import Zones

left_side_item = LeftSideMenu.objects.all()

# Create your views here.
def zones(request):
    
    
    all_zones = Zones.objects.all();

    return render(request, 'menu/zones.html',
                  {'left_side_item': left_side_item, 
                   'all_zones':all_zones } )
    
def dorion(request):
    
    dorion = Zones.objects.all().filter(name="Dorion");
    
    return render(request, 'zones/dorion.html',
                  {'left_side_item': left_side_item, 
                   'dorion':dorion} )
    
def protean(request):
    
    protean = Zones.objects.all().filter(name="Protean Kingdom");
    
    return render(request, 'zones/protean.html',
                  {'left_side_item': left_side_item, 
                   'protean':protean} )
    
def lunaskar(request):
    
    lunaskar = Zones.objects.all().filter(name="Lunaskar Kingdom");
    
    return render(request, 'zones/lunaskar.html',
                  {'left_side_item': left_side_item, 
                   'lunaskar':lunaskar} )
    
def haggar(request):
    
    haggar = Zones.objects.all().filter(name="Haggar Castle");
    
    return render(request, 'zones/haggar.html',
                  {'left_side_item': left_side_item, 
                   'haggar':haggar} )
    
def haddar(request):
    
    haddar = Zones.objects.all().filter(name="Haddar Castle");
    
    return render(request, 'zones/haddar.html',
                  {'left_side_item': left_side_item, 
                   'haddar':haddar} )
    
def death_valley(request):
    
    death_valley = Zones.objects.all().filter(name="Death Valley");
    
    return render(request, 'zones/death_valley.html',
                  {'left_side_item': left_side_item, 
                   'death_valley':death_valley} )
    
    
def narun_tower(request):
    
    narun_tower = Zones.objects.all().filter(name="Narun Tower");
    
    return render(request, 'zones/narun_tower.html',
                  {'left_side_item': left_side_item, 
                   'narun_tower':narun_tower} )