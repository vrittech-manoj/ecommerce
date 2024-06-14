from django.contrib import admin
from django.urls import path,include

from . import views 

urlpatterns = [
    path('contact-us/',views.MyContact,name='contact_us'),
    path('save-contact-us/',views.SaveContact,name='save_contact_us'),
]
