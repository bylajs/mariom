from django import forms
from django.contrib.auth.models import User 
from .models import UserProfile

class ModificaProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
        widgets = {
               'email' : forms.EmailInput(
                  attrs={
                  'class': 'form-control'
                    }
                ),
             'first_name' : forms.TextInput(
                            attrs={
                            'class': 'form-control',
                    }
                ),
                 'last_name' : forms.TextInput(
                            attrs={
                            'class': 'form-control',
                    }
                ),
                    }

class UProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'image','indirizzo','citta','paese','ecap','descrizione','ruolo',
        )
        widgets = {
                 'descrizione' : forms.Textarea(attrs={"rows":5, "cols":20})
                    }
