from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'fat','calorie',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            
            'calorie': forms.TextInput(attrs={'class':'form-control'}),
            'fat': forms.TextInput(attrs={'class':'form-control'}),
            
            

        }