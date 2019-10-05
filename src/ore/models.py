from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils.translation import ugettext as _


# Create your models here.
 
class Ore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ore",null=True,)
    data = models.DateField(default=timezone.now)
    oret = models.FloatField()
    contrattiok = models.PositiveSmallIntegerField()
    contrattiko = models.PositiveSmallIntegerField(default=0,)
    nomecognome = models.CharField(max_length=100,blank=True)
    InLavorazione = 'In Lavorazione'
    CheckCallok = 'Check Call Ok'
    CheckCallko = 'Check Call Ko'
    Moroso      = 'Moroso'
    Ripensamento = 'Ripensamento'
    InAttivazione = 'In Attivazione'
    Rispinto = 'Rispinto'
    Attivo = 'Attivo'
    Recesso = 'Recesso'
    status = [
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
    statuse = models.CharField(
        max_length=200,
        choices=status,
        default=InLavorazione,
    )

    class Meta:  
        db_table = "ore"
        ordering = ('-data',)
        permissions = (
            ('is_operatore', _('Is Operatore')),
            ('is_supervizore', _('Is Supervizore')),
        )


    def __str__(self):
        return self.user.username 

