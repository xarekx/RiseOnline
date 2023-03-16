from django.shortcuts import render
from menu.models import LeftSideMenu
from zones.models import Zone

left_side_item = LeftSideMenu.objects.all().order_by("priority")

# Create your views here.
def zones(request):
    
    
    all_zones = Zone.objects.all();

    return render(request, 'menu/zones.html',
                  {'left_side_item': left_side_item, 
                   'all_zones':all_zones } )
    
def dorion(request):
    
    dorion = Zone.objects.all().filter(name="Dorion");
    
    return render(request, 'zones/dorion.html',
                  {'left_side_item': left_side_item, 
                   'dorion':dorion} )
    
def protean(request):
    
    protean = Zone.objects.all().filter(name="Protean Kingdom");
    
    return render(request, 'zones/protean.html',
                  {'left_side_item': left_side_item, 
                   'protean':protean} )
    
def lunaskar(request):
    
    lunaskar = Zone.objects.all().filter(name="Lunaskar Kingdom");
    
    return render(request, 'zones/lunaskar.html',
                  {'left_side_item': left_side_item, 
                   'lunaskar':lunaskar} )
    
def haggar(request):
    
    haggar = Zone.objects.all().filter(name="Haggar Castle");
    
    return render(request, 'zones/haggar.html',
                  {'left_side_item': left_side_item, 
                   'haggar':haggar} )
    
def haddar(request):
    
    haddar = Zone.objects.all().filter(name="Haddar Castle");
    
    return render(request, 'zones/haddar.html',
                  {'left_side_item': left_side_item, 
                   'haddar':haddar} )
    
def death_valley(request):
    
    death_valley = Zone.objects.all().filter(name="Death Valley");
    
    return render(request, 'zones/death_valley.html',
                  {'left_side_item': left_side_item, 
                   'death_valley':death_valley} )
    
    
def narun_tower(request):
    
    narun_tower = Zone.objects.all().filter(name="Narun Tower");
    
    return render(request, 'zones/narun_tower.html',
                  {'left_side_item': left_side_item, 
                   'narun_tower':narun_tower} )