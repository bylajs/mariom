from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ore 


class CreateNewOreupdate(forms.ModelForm):
      class Meta:  
            model = Ore
            fields = ('oret','contrattiok','contrattiko','nomecognome','statuse',)
            widgets = {
                 'data' : forms.DateInput(
                attrs={
               'class': 'md-form'
                    }
                ),
                'user' : forms.Select(
                attrs={
                'class': 'custom-select',
                    }
                ),
                'contrattiok' : forms.NumberInput(
                attrs={
                'class': 'form-control',
                    }
                ),               
                'oret' : forms.NumberInput(
                attrs={
                'class': 'form-control'
                    }
                ),
                'nomecognome' : forms.TextInput(
                attrs={
                'class': 'form-control'
                    }
                ),   
                }  

class CreateNewOre(forms.ModelForm):
      class Meta:  
            model = Ore 
            exclude = ('statuse','contrattiko', ) 
            fields = ('user','oret','contrattiok','contrattiko','nomecognome','statuse',)
            widgets = {
                 'data' : forms.DateInput(
                attrs={
               'class': 'md-form'
                    }
                ),
                'user' : forms.Select(
                attrs={
                'class': 'custom-select',
                    }
                ),
                'contrattiok' : forms.NumberInput(
                attrs={
                'class': 'form-control'
                    }
                ),               
                'oret' : forms.NumberInput(
                attrs={
                'class': 'form-control'
                    }
                ),
                'nomecognome' : forms.TextInput(
                attrs={
                'class': 'form-control'
                    }
                ),  
                }   
