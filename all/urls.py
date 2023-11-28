from django.contrib import admin
from django.urls import path
from all import views as all_views

urlpatterns = [
    path('', all_views.home, name='home'),
    path('contact/', all_views.contact, name='contact'),
    path('about/', all_views.about, name='about'),
    path('services/', all_views.services, name='services'),
    path('projects/', all_views.projects, name='projects'),
    path('send-email/', all_views.sendemail, name='emailus'),
]
