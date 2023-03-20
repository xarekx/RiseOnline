from django.shortcuts import render, HttpResponseRedirect
from menu.models import LeftSideMenu
from contacts.forms import ContactForm

def contacts(request):
    
    form = ContactForm(request.POST)
    
   
    left_side_item = LeftSideMenu.objects.all().order_by("priority")
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contacts/')
   
    
    return render(request, 'menu/contacts.html', { 'left_side_item':left_side_item,'form':form})
