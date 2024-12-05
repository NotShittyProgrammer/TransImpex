from django import forms
from .models import Communication, Consultation


class Contact(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ['name', 'email', 'topic', 'description', 'file']


class Consultation_form(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['email', 'name']
