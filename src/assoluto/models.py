from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
import random
import string
import datetime
import decimal
from random import randint
random_string = str(random.randint(100000, 999999))
def random_string(): 
    return randint(100000, 999999)  

# Create your models here.
   
    


class Contratti(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contratti",null=True)
    edata = models.DateField(default=timezone.now)
    enome = models.CharField(max_length=100)  
    ecognome = models.CharField(max_length=100)
    ecodicefiscale = models.CharField(max_length=16)
    enumero = models.CharField(max_length=10)
    etelefono = models.CharField(max_length=12)
    ecellulare = models.CharField(max_length=10)   
    eemail = models.EmailField()
    evia = models.CharField(max_length=300)
    ecivico = models.CharField(max_length=6)
    ecap = models.CharField(max_length=5)
    ecomune = models.CharField(max_length=300)
    eprovincia = models.CharField(max_length=300)
    efornitore = models.CharField(max_length=29,blank=True,)
    epod = models.CharField(max_length=14,blank=True,)
    epotenzaimpegnata = models.CharField(max_length=4,blank=True,)
    epotenzadisponibile = models.CharField(max_length=4,blank=True,)
    econsumoannuo = models.CharField(max_length=6,blank=True,)
    eviafornitura = models.CharField(max_length=300,blank=True,)
    ecivicofornitura = models.CharField(max_length=6,blank=True,)
    ecapfornitura = models.CharField(max_length=5,blank=True,)
    ecomunefornitura = models.CharField(max_length=300,blank=True,)
    eprovinciafornitura = models.CharField(max_length=300,blank=True,)
    efornitoregas = models.CharField(max_length=29,blank=True,)
    epdr = models.CharField(max_length=14,blank=True,)
    eremi = models.CharField(max_length=12,blank=True,)
    ematricola = models.CharField(max_length=100,blank=True,)
    eprontointervento = models.CharField(max_length=9,blank=True,)
    econsumoannuogas = models.CharField(max_length=6,blank=True,)
    eviagas = models.CharField(max_length=300,blank=True,)
    ecivicogas = models.CharField(max_length=6,blank=True,)
    ecapgas = models.CharField(max_length=5,blank=True,)
    ecomunegas = models.CharField(max_length=300,blank=True,)
    eprovinciagas = models.CharField(max_length=300,blank=True,)
    iban = models.CharField(null=True, blank=True, max_length=27)
    ecarica = models.FileField(upload_to='rec/')
    numerocliente = models.CharField(default = random_string,max_length=1000000,unique=True)
 
 ###dataattivazione Model
    Gennaio = '1 Gennaio'
    Febbraio = '1 Febbraio'
    Marzo = '1 Marzo'
    Aprile = '1 Aprile'
    Maggio= '1 Maggio'
    Giugno = '1 Giugno'
    Luglio = '1 Luglio'
    Agosto = '1 Agosto'
    Settembre = '1 Settembre'
    Ottobre = '1 Ottobre'
    Novembre = '1 Novembre'
    Dicembre = '1 Dicembre'
    stimaattivazione = [
        ('', 'Seleziona Data Di Attivazione '),
        (Gennaio, '1 Gennaio'),
        (Febbraio, '1 Febbraio'),
        (Marzo, '1 Marzo'),
        (Aprile, '1 Aprile'),
        (Maggio, '1 Maggio'),
        (Giugno, '1 Giugno'),
        (Luglio, '1 Luglio'),
        (Agosto, '1 Agosto'),
        (Settembre, '1 Settembre'),
        (Ottobre, '1 Ottobre'),
        (Novembre, '1 Novembre'),
        (Dicembre, '1 Dicembre'),
    ]
    eattivazione = models.CharField(
        max_length=200,
        choices=stimaattivazione,

    )


#Operatore Model
    Alkmeda = 'Alkmeda Bylaj'
    Marino = 'Marinario Mustafa'
    Bledi = 'Bledar Zeneli'
    Tao = 'Taulant Nushi'
    Arjan = 'Arjan Bylaj'
    Ilda = 'Ilda Meco'
    Denisa = 'Denisa Shuteriqi'
    operatore = [
        ('', 'Seleziona Operatore'),
        (Alkmeda, 'Alkmeda Bylaj'),
        (Marino, 'Marinario Mustafa'),
        (Bledi, 'Bledar Zeneli'),
        (Tao, 'Taulant Nushi'),
        (Arjan, 'Arjan Bylaj'),
        (Ilda, 'Ilda Meco'),
        (Denisa, 'Denisa Shuteriqi'),
    ]
    eoperatore = models.CharField(
        max_length=200,
        choices=operatore,

    )
#Supervizore Model
    Alkmeda = 'Alkmeda Bylaj'
    supervizore = [
        ('', 'Seleziona Supervizore'),
        (Alkmeda, 'Alkmeda Bylaj'),
    ]
    esupervizore = models.CharField(
        max_length=200,
        choices=supervizore,

    )
#Documento Model 
    CartaDiIdentita = 'Carta Di Identita'
    Patente = 'Patente'
    documento = [
        ('', 'Seleziona Documento'),
        (CartaDiIdentita, 'Carta Di Identita'),
        (Patente, 'Patente'),
    ]
    edocumento = models.CharField(
        max_length=200,
        choices=documento,

    )
#Tipologia Cliente Model 
    DomesticoResidente = 'Domestico Residente'
    DomesticoNonResidente = 'Domestico Non Residente'
    AltriUsi = 'Altri Usi'
    tipologia = [
        ('', 'Seleziona Tipologia Cliente'),
        (DomesticoResidente, 'Domestico Residente'),
        (DomesticoNonResidente, 'Domestico Non Residente'),
        (AltriUsi, 'Altri Usi'),
    ]
    etipologia = models.CharField(
        max_length=200,
        choices=tipologia,
        blank=True,

    )
#Tipologia D'uso Gas
    RCA = 'Riscaldamento + Cottura + Acqua Calda'
    RC = 'Riscaldamento + Cottura'
    RA = 'Riscaldamento + Acqua Calda'
    CA = 'Cottura + Acqua Calda'
    R = 'Solo Riscaldamento'
    C = 'Solo Cottura'
    A = 'Solo Acqua Calda'
    tipologiaduso = [
        ('', 'Seleziona Tipologia D-Uso'),
        (RCA, 'Riscaldamento + Cottura + Acqua Calda'),
        (RC, 'Riscaldamento + Cottura'),
        (RA, 'Riscaldamento + Acqua Calda'),
        (CA, 'Cottura + Acqua Calda'),
        (R, 'Solo Riscaldamento'),
        (C, 'Solo Cottura'),
        (A, 'Solo Acqua Calda'),
    ]
    etipologiaduso = models.CharField(
        max_length=200,
        choices=tipologiaduso,
        blank=True,

    )
#Modalita Di Pagamento Model
    Bolletino = 'Bolletino'
    Rid = 'Rid'
    modalita = [
        ('', 'Seleziona Modalita Di Pagamento'),
        (Bolletino, 'Bolletino'),
        (Rid, 'Rid'),
    ]
    emodalita = models.CharField(
        max_length=200,
        choices=modalita,


    )
#Pubblicita Model 
    No = 'No'
    Si = 'Si'
    pubblicita = [
        (No, 'No'),
        (Si, 'Si'),
    ]
    epubblicita = models.CharField(
        max_length=200,
        choices=pubblicita,
        default=No,
    )
#Indirizzo Spedizione Fatture Model 
    AlIndirizzoDiResidenza = 'Al Indirizzo Di Residenza'
    TramiteEmail = 'Tramite Email'
    AlIndirizzoDiFornitura = 'Al Indirizzo Di Fornitura'
    indirizzospedizione = [
        ('', 'Seleziona Spedizione Fatture'),
        (AlIndirizzoDiResidenza, 'Al Indirizzo Di Residenza'),
        (TramiteEmail, 'Tramite Email'),
        (AlIndirizzoDiFornitura, 'Al Indirizzo Di Fornitura'),
    ]
    eindirizzospedizione = models.CharField(
        max_length=200,
        choices=indirizzospedizione,

    )
#contratto Luce Model 
    Luce = 'Luce'
    Gas = 'Gas'
    Dual = 'Dual'
    contratto = [
        (Luce, 'Luce'),
        (Gas, 'Gas'),
        (Dual, 'Dual'),
    ]
    econtratto = models.CharField(
        max_length=200,
        choices=contratto, 
    )
# Esito
    InLavorazione = 'In Lavorazione'
    CheckCallok = 'Check Call Ok'
    CheckCallko = 'Check Call Ko'
    Moroso      = 'Moroso'
    Ripensamento = 'Ripensamento'
    InAttivazione = 'In Attivazione'
    Rispinto = 'Rispinto'
    Attivo = 'Attivo'
    Recesso = 'Recesso'
    esitos = [
        (InLavorazione, 'In Lavorazione'),
        (CheckCallok, 'Check Call Ok'),
        (CheckCallko, 'Check Call Ko'),
        (Moroso, 'Moroso'),
        (Ripensamento, 'Ripensamento'),
        (InAttivazione, 'In Attivazione'),
        (Rispinto, 'Rispinto'),
        (Attivo, 'Attivo'),
        (Recesso, 'Recesso'),
    ]
    esito = models.CharField(
        max_length=200,
        choices=esitos,
        default=InLavorazione,

    )



    class Meta:  
        db_table = "contratti"
        ordering = ('-edata',)
