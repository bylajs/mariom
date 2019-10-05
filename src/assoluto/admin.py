from django.contrib import admin

# Register your models here.
from .models import Contratti  
from .forms import LuceForm 



admin.site.register(Contratti)
 
