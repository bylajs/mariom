from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contratti
 
             
class RegisterForm(UserCreationForm):
      class Meta:  
            model = User  
            fields = ('username','password1','password2')

class LuceForm(forms.ModelForm):
    class Meta:
        model = Contratti
        exclude = ('esito',)
        fields = ('eattivazione','econtratto','eoperatore','esupervizore','enome','ecognome','ecodicefiscale','edocumento','enumero','eemail','etelefono','ecellulare','evia','ecivico','ecap','ecomune','eprovincia','efornitore','epod','eviafornitura','ecivicofornitura','ecapfornitura','ecomunefornitura','eprovinciafornitura','epotenzaimpegnata','epotenzadisponibile','econsumoannuo','etipologia','emodalita','iban','eindirizzospedizione','epubblicita','ecarica',)
        widgets = {
                'user' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'edata' : forms.DateInput(
				attrs={
				'class': 'md-form'
					}
				),
                'eattivazione' : forms.Select(
                attrs={
                'class': 'custom-select','required': True,
                    }
                ),
                'eoperatore' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'esupervizore' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'enome' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecognome' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecodicefiscale' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,'minlength' : '16',
                    }
                ),
                'edocumento' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'enumero' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'placeholder' : 'Documento Numero','minlength' : '9','required': True,
                    }
                ),
                'eemail' : forms.EmailInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'etelefono' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+','required': True,
                    }
                ),
                'ecellulare' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+', 'minlength' : '9', 'required': True,
                    }
                ),

               'evia' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecivico' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecap' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eprovincia' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecomune' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'efornitore' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ), 
                'epod' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14','required': True,
                    }
                ),
               'eviafornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecivicofornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecapfornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eprovinciafornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecomunefornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'epotenzaimpegnata' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'epotenzadisponibile' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'econsumoannuo' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'etipologia' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'emodalita' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),

                'iban' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '27',
                    }
                ),
                'eindirizzospedizione' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),

                'epubblicita' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),

                'econtratto' :  forms.HiddenInput(
                            attrs={
                            'class' : "custom-select",
                    }
                ), 
			} 
############ Fine Contratto Luce ##############################

class GasForm(forms.ModelForm):
    class Meta:
        model = Contratti 
        exclude = ('esito',)
        fields = ('eattivazione','eoperatore','esupervizore','enome','ecognome','ecodicefiscale','edocumento','enumero','eemail','etelefono','ecellulare','evia','ecivico','ecap','ecomune','eprovincia','efornitoregas','eviagas','ecivicogas','ecapgas','ecomunegas','eprovinciagas','epdr','eremi','ematricola','eprontointervento','econsumoannuogas','etipologiaduso','emodalita','iban','eindirizzospedizione','epubblicita','econtratto','ecarica',)
        widgets = {
                'user' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'edata' : forms.DateInput(
                attrs={
                'class': 'md-form'
                    }
                ),
                'eattivazione' : forms.Select(
                attrs={
                'class': 'custom-select','required': True,
                    }
                ),
                'eoperatore' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'esupervizore' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'enome' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecognome' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecodicefiscale' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,'minlength' : '16',
                    }
                ),
                'edocumento' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'enumero' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'placeholder' : 'Documento Numero','minlength' : '9','required': True,
                    }
                ),
                'eemail' : forms.EmailInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'etelefono' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+','required': True,
                    }
                ),
                'ecellulare' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+', 'minlength' : '9','required': True,
                    }
                ),

                'evia' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecivico' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecap' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eprovincia' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecomune' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'efornitoregas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'epdr' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14','required': True,
                    }
                ),
                'eviagas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecivicogas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecapgas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eprovinciagas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecomunegas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eremi' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '8','required': True,
                    }
                ),
                'ematricola' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eprontointervento' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '9','required': True,
                    }
                ),
                'etipologiaduso' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'econsumoannuogas' :  forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'emodalita' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),

                'iban' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '27',
                    }
                ),
                'eindirizzospedizione' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),

                'epubblicita' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),

                'econtratto' :  forms.HiddenInput(
                            attrs={
                            'class' : "custom-select" 
                    }
                ), 
            }

############ Fine Contratto Gas ##############################

class DualForm(forms.ModelForm):
    class Meta:
        model = Contratti 
        exclude = ('esito',)
        fields = ('eattivazione','eoperatore','esupervizore','enome','ecognome','ecodicefiscale','edocumento','enumero','eemail','etelefono','ecellulare','evia','ecivico','ecap','ecomune','eprovincia','efornitore','epod','eviafornitura','ecivicofornitura','ecapfornitura','ecomunefornitura','eprovinciafornitura','epotenzaimpegnata','epotenzadisponibile','econsumoannuo','etipologia','efornitoregas','eviagas','ecivicogas','ecapgas','ecomunegas','eprovinciagas','epdr','eremi','ematricola','eprontointervento','econsumoannuogas','etipologiaduso','emodalita','iban','eindirizzospedizione','epubblicita','econtratto','ecarica',)
        widgets = {
                'user' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'edata' : forms.DateInput(
                attrs={
                'class': 'md-form'
                    }
                ),
                'eattivazione' : forms.Select(
                attrs={
                'class': 'custom-select','required': True,
                    }
                ),
                'eoperatore' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'esupervizore' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'enome' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecognome' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'ecodicefiscale' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,'minlength' : '16',
                    }
                ),
                'edocumento' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'enumero' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'placeholder' : 'Documento Numero','minlength' : '9','required': True,
                    }
                ),
                'eemail' : forms.EmailInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'etelefono' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+','required': True,
                    }
                ),
                'ecellulare' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+', 'minlength' : '9','required': True,
                    }
                ),
                'epod' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,'minlength' : '14',
                    }
                ),
                
                'evia' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecivico' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecap' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'eprovincia' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecomune' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'efornitore' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ), 
                'epdr' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14','required': True,
                    }
                ),
               'eviafornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecivicofornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecapfornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'eprovinciafornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecomunefornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'epotenzaimpegnata' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'epotenzadisponibile' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'econsumoannuo' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'etipologia' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'efornitoregas' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'epdr' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14','required': True,
                    }
                ),
                'eviagas' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecivicogas' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecapgas' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'eprovinciagas' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'ecomunegas' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'required': True,
                    }
                ),
                'eremi' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '8','required': True,
                    }
                ),
                'ematricola' : forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'eprontointervento' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '9','required': True,
                    }
                ),
                'etipologiaduso' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),
                'econsumoannuogas' :  forms.TextInput(
                            attrs={
                            'class': 'form-control','required': True,
                    }
                ),
                'emodalita' : forms.Select(
                            attrs={
                            'class': 'custom-select','required': True,
                    }
                ),
                'iban' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '27',
                    }
                ),
                'eindirizzospedizione' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),

                'epubblicita' :  forms.Select(
                            attrs={
                            'class' : "custom-select",'required': True,
                    }
                ),

                'econtratto' :  forms.HiddenInput(
                            attrs={
                            'class' : "custom-select" 
                    }
                ), 
            }
class DualFormUpdate(forms.ModelForm):
    class Meta:
        model = Contratti 
        fields = ('eattivazione','esito','eoperatore','esupervizore','enome','ecognome','ecodicefiscale','edocumento','enumero','eemail','etelefono','ecellulare','evia','ecivico','ecap','ecomune','eprovincia','efornitore','epod','eviafornitura','ecivicofornitura','ecapfornitura','ecomunefornitura','eprovinciafornitura','epotenzaimpegnata','epotenzadisponibile','econsumoannuo','etipologia','efornitoregas','eviagas','ecivicogas','ecapgas','ecomunegas','eprovinciagas','epdr','eremi','ematricola','eprontointervento','econsumoannuogas','etipologiaduso','emodalita','iban','eindirizzospedizione','epubblicita','econtratto','ecarica',)
        widgets = {
                'user' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'edata' : forms.DateInput(
                attrs={
                'class': 'md-form'
                    }
                ),
                'eattivazione' : forms.Select(
                attrs={
                'class': 'custom-select'
                    }
                ),
                'eoperatore' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'esupervizore' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'enome' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecognome' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecodicefiscale' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '16',
                    }
                ),
                'edocumento' :  forms.Select(
                            attrs={
                            'class' : "custom-select"
                    }
                ),
                'enumero' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'placeholder' : 'Documento Numero','minlength' : '9',
                    }
                ),
                'eemail' : forms.EmailInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'etelefono' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+',
                    }
                ),
                'ecellulare' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'pattern':'[0-9]+', 'minlength' : '9',
                    }
                ),
                'epod' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14',
                    }
                ),
                
                'evia' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecivico' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecap' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'eprovincia' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecomune' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'efornitore' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ), 
                'epdr' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14',
                    }
                ),
               'eviafornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecivicofornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecapfornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'eprovinciafornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecomunefornitura' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'epotenzaimpegnata' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'epotenzadisponibile' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'econsumoannuo' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'etipologia' :  forms.Select(
                            attrs={
                            'class' : "custom-select"
                    }
                ),
                'efornitoregas' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'epdr' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '14',
                    }
                ),
                'eviagas' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecivicogas' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecapgas' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'eprovinciagas' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'ecomunegas' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'eremi' : forms.TextInput(
                            attrs={
                            'class': 'form-control','minlength' : '8',
                    }
                ),
                'ematricola' : forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'eprontointervento' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '9',
                    }
                ),
                'etipologiaduso' :  forms.Select(
                            attrs={
                            'class' : "custom-select"
                    }
                ),
                'econsumoannuogas' :  forms.TextInput(
                            attrs={
                            'class': 'form-control'
                    }
                ),
                'emodalita' : forms.Select(
                            attrs={
                            'class': 'custom-select'
                    }
                ),
                'iban' : forms.TextInput(
                            attrs={
                            'class': 'form-control', 'minlength' : '27',
                    }
                ),
                'eindirizzospedizione' :  forms.Select(
                            attrs={
                            'class' : "custom-select"
                    }
                ),

                'epubblicita' :  forms.Select(
                            attrs={
                            'class' : "custom-select"
                    }
                ),
                'econtratto' :  forms.Select(
                            attrs={
                            'class' : "custom-select" 
                    }
                ),
                 'esito' :  forms.Select(
                            attrs={
                            'class' : "custom-select" 
                    }
                ),  
            }
