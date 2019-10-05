from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ModificaProfileForm,UProfileForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Crate your views here. 

@login_required(login_url='/login/') 
def modificaprofilo(request):
    if request.method == 'POST':
        u_form = ModificaProfileForm(request.POST,request.FILES, instance=request.user)
        p_form = UProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profilo Aggiornato con successo.')
            return render(request, 'modificaprofilo.html')

    else:
        u_form = ModificaProfileForm(instance=request.user)
        p_form = UProfileForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'modificaprofilo.html', context)
 
