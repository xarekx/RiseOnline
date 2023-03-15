from django.urls import path, include
from contacts.views import contacts

urlpatterns = [
    path('', contacts, name="contacts")
]