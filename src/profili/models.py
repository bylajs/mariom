from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone 
# Create your models here.





class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    indirizzo = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    paese = models.CharField(max_length=50) 
    ecap = models.CharField(max_length=4)
    descrizione = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='profile_image', blank=True,null=True)
    #ruoli
    Operatore = 'Operatore'
    Supervizore = 'Supervizore'
    Cordinatore = 'Cordinatore'
    Backoffice = 'Backoffice'
    Direttore = 'Direttore'
    Presidente = 'Presidente'
    ruoli = [
        (Operatore, 'Operatore'),
        (Supervizore, 'Supervizore'),
        (Cordinatore, 'Cordinatore'),
        (Backoffice, 'Backoffice'),
        (Direttore, 'Direttore'),
        (Presidente, 'Presidente'),
    ]
    ruolo = models.CharField(
        max_length=200,
        choices=ruoli,
        default=Operatore,
    )

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
