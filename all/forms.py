from django import forms
from django.forms import ModelForm
from all.models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
