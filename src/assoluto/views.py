from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import When, F, Q
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from django.db.models import IntegerField, F, Case, When
from django.db.models import Value
from django.db.models import  Case
from .forms import RegisterForm
from .models import Contratti
from .forms import LuceForm
from .forms import GasForm
from .forms import DualForm,DualFormUpdate
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone 
from ore.models import Ore
from django.db.models.functions import Coalesce
import django
import csv 
# Create your views here. 
# Kjo eshte HomePage.


@login_required(login_url='/login/')
def inizio(request): 
    this_month = datetime.now().month
    users = User.objects.filter(ore__data__month=this_month).annotate(total_contrattiok=Coalesce(Sum('ore__contrattiok'), (0))).order_by('-total_contrattiok')
    count = User.objects.filter().count()
    supervizori = User.objects.filter(is_staff=True).count() 
    this_month = datetime.now().month
    oktuttohome = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiok"), (0)))
    kotuttoohome = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiko"), (0)))
    this_month = datetime.now().month
    tutto = Contratti.objects.filter(edata__month=this_month).count()
    luce = Contratti.objects.filter(econtratto='Luce',edata__month=this_month).count()
    gas = Contratti.objects.filter(econtratto='Gas',edata__month=this_month).count()
    dual = Contratti.objects.filter(econtratto='Dual',edata__month=this_month).count()
    now = timezone.now()
    tuttooggi = Contratti.objects.filter(edata__day=now.day).count()
    luceoggi = Contratti.objects.filter(econtratto='Luce',edata__day=now.day).count()
    gasoggi = Contratti.objects.filter(econtratto='Gas',edata__day=now.day).count()
    dualoggi = Contratti.objects.filter(econtratto='Dual',edata__day=now.day).count()
    return render (request, "base.html", {"supervizori":supervizori,"count":count,"oktuttohome":oktuttohome,"kotuttoohome":kotuttoohome,"luce":luce,"gas":gas,"dual":dual,"tutto":tutto,"users":users,"luceoggi":luceoggi,"gasoggi":gasoggi,"dualoggi":dualoggi,"tuttooggi":tuttooggi,})

@login_required(login_url='/login/') 
def register(response):
    if not response.user.is_staff:
       return redirect('/error_404')
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save()
            messages.success(response,'Account Creato Con Successo')
        return redirect('/register')
    else:
            form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

@login_required(login_url='/login/') 
def luce(request):
    if not request.user.is_staff:
       return redirect('/error_404')
    if request.method == "POST": 
        form = LuceForm(request.POST, request.FILES)
        epod = request.POST['epod']
        if Contratti.objects.filter(epod=epod).exists():
            messages.error(request,'Pod Gia Presente Nel Sistema')
            return redirect('/luce')
        else:
            if form.is_valid():
                try:
                    contratti = form.save(commit=False)
                    contratti.user = request.user
                    contratti.save()
                    messages.success(request, 'Contratto Inserito Con Successo.')
                    return redirect('/luce')
                except:
                    pass  
    else:  
        form = LuceForm()  
    return render(request,'index.html',{'form':form})

@login_required(login_url='/login/') 
def gas(request):
    if not request.user.is_staff:
       return redirect('/error_404')  
    if request.method == "POST":  
        form = GasForm(request.POST, request.FILES) 
        epdr = request.POST['epdr']
        if Contratti.objects.filter(epdr=epdr).exists():
            messages.error(request,'Pdr Gia Presente Nel Sistema')
            return redirect('/gas')   
        if form.is_valid():  
            try:  
                contratti = form.save(commit=False)
                contratti.user = request.user
                contratti.save() 
                messages.success(request, 'Contratto Inserito Con Successo.')
                return redirect('/gas')   
            except:  
                pass  
    else:  
        form = GasForm()  
    return render(request,'gas.html',{'form':form})

@login_required(login_url='/login/') 
def dual(request):
    if not request.user.is_staff:
       return redirect('/error_404')
    if request.method == "POST":  
        form = DualForm(request.POST, request.FILES)
        epod = request.POST['epod']
        epdr = request.POST['epdr']
        if Contratti.objects.filter(epod=epod).exists():
            messages.error(request,'Pod Gia Presente Nel Sistema')
            return redirect('/dual')
        if Contratti.objects.filter(epdr=epdr).exists():
            messages.error(request,'Pdr Presente Nel Sistema')
            return redirect('/dual')    
        if form.is_valid():  
            try:  
                contratti = form.save(commit=False)
                contratti.user = request.user
                contratti.save()
                messages.success(request, 'Contratto Inserito Con Successo.')
                return redirect('/dual')
            except:  
                pass  
    else:  
        form = DualForm()  
    return render(request,'dual.html',{'form':form})

@login_required(login_url='/login/') 
def show(request):
    if not request.user.is_staff:
       return redirect('/error_404')  
    contratta = Contratti.objects.filter(user=request.user)
    contratta_list = Contratti.objects.filter(user=request.user)
    this_month = datetime.now().month
    svinlavorazione = Contratti.objects.filter(esito='In Lavorazione',edata__month=this_month).count()
    svqcok = Contratti.objects.filter(esito='Check Call Ok',edata__month=this_month).count()
    svqcko = Contratti.objects.filter(esito='Check Call Ko',edata__month=this_month).count()
    svmoroso = Contratti.objects.filter(esito='Moroso',edata__month=this_month).count()
    page = request.GET.get('page', 1)

    paginator = Paginator(contratta_list, 7)
    try:
        contratta = paginator.page(page)
    except PageNotAnInteger:
        contratta = paginator.page(1)
    except EmptyPage:
        contratta = paginator.page(paginator.num_pages)  
    return render(request,"show.html",{'contratta':contratta,'svinlavorazione':svinlavorazione,'svqcok':svqcok,'svqcko':svqcko,'svmoroso':svmoroso})  

@login_required(login_url='/login/') 
def edit(request, id):
    if not request.user.is_staff:
       return redirect('/error_404')  
    contratti = Contratti.objects.get(id=id)  
    return render(request,'edit.html', {'contratti':contratti})
@login_required(login_url='/login/') 
def vedi(request, id):  
    if not request.user.is_staff:
       return redirect('/error_404')   
    contratti = Contratti.objects.get(id=id)  
    return render(request,'vedi.html', {'contratti':contratti})

@login_required(login_url='/login/') 
def update(request, id):
    if not request.user.is_staff:
       return redirect('/error_404')   
    contratti = Contratti.objects.get(id=id)  
    form = DualFormUpdate(request.POST, instance = contratti)  
    if form.is_valid():  
        form.save()
        messages.success(request, 'Scheda Aggiornata con successo.')  
        return redirect("/show")  
    return render(request, 'edit.html', {'contratti': contratti})
    
@login_required(login_url='/login/') 
def destroy(request, id):
    if not request.user.is_staff:
       return redirect('/error_404')   
    contratti = Contratti.objects.get(id=id)  
    if request.method == "POST":
        contratti.delete()
        messages.success(request, 'Scheda Cancellata con successo.')
        return redirect('/show')
    context = {
        "contratti": contratti
    }
    return render(request, "cancella-contratto.html", context)

def is_valid_queryparam(param):
    return param != '' and param is not None

      
@login_required(login_url='/login/') 
def cerca(request):
    if not request.user.is_staff:
       return redirect('/error_404') 
    qs = Contratti.objects.filter(user=request.user)
    this_month = datetime.now().month
    svinlavorazione = Contratti.objects.filter(esito='In Lavorazione',edata__month=this_month).count()
    svqcok = Contratti.objects.filter(esito='Check Call Ok',edata__month=this_month).count()
    svqcko = Contratti.objects.filter(esito='Check Call Ko',edata__month=this_month).count()
    svmoroso = Contratti.objects.filter(esito='Moroso',edata__month=this_month).count()
    epod = request.GET.get('epod')
    epdr = request.GET.get('epdr')
    ecodicefiscale = request.GET.get('ecodicefiscale')
    eoperatore = request.GET.get('eoperatore')
    enome = request.GET.get('enome')
    ecognome = request.GET.get('ecognome')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')


    if is_valid_queryparam(epod):
        qs = qs.filter(epod=epod)

    if is_valid_queryparam(epdr):
        qs = qs.filter(epdr=epdr)

    if is_valid_queryparam(ecodicefiscale):
        qs = qs.filter(ecodicefiscale=ecodicefiscale)

    if is_valid_queryparam(eoperatore):
        qs = qs.filter(eoperatore=eoperatore)

    if is_valid_queryparam(enome):
        qs = qs.filter(enome=enome)

    if is_valid_queryparam(ecognome):
        qs = qs.filter(ecognome=ecognome)

    if is_valid_queryparam(date_min):
        qs = qs.filter(edata__gte=date_min) 

    if is_valid_queryparam(date_max): 
        qs = qs.filter(edata__lte=date_max)

    context = {
        'contratta': qs,
        'svinlavorazione':svinlavorazione,
        'svqcok':svqcok,
        'svqcko':svqcko,
        'svmoroso':svmoroso,
        }
    return render(request, "show.html", context)

@login_required(login_url='/login/') 
def error_404(request):  
    return render(request,'error_404.html')


@login_required(login_url='/login/')  
def export_contratti_csv(request):
    if not request.user.is_staff:
       return redirect('/error_404')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contratta.csv"'

    writer = csv.writer(response)
    writer.writerow(['user_id', 'esupervizore', 'eoperatore', 'edata', 'numerocliente', 'econtratto', 'enome', 'ecognome', 'ecodicefiscale', 'etelefono', 'ecellulare', 'eemail'
        , 'edocumento', 'enumero', 'evia', 'ecivico', 'ecap', 'ecomune', 'eprovincia', 'efornitore', 'epod', 'etipologia', 'epotenzaimpegnata', 'epotenzadisponibile'
        , 'eviafornitura', 'ecivicofornitura', 'ecapfornitura', 'ecomunefornitura', 'eprovinciafornitura', 'econsumoannuo', 'efornitoregas', 'epdr', 'eremi'
        , 'ematricola', 'eprontointervento', 'etipologiaduso', 'eviagas', 'ecivicogas', 'ecapgas', 'ecomunegas', 'eprovinciagas', 'econsumoannuogas', 'emodalita',
        'iban', 'eindirizzospedizione', 'eattivazione', 'epubblicita', 'esito', 'ecarica',])

    contratta = Contratti.objects.all().values_list('user_id', 'esupervizore', 'eoperatore', 'edata', 'numerocliente', 'econtratto', 'enome', 'ecognome', 'ecodicefiscale', 'etelefono', 'ecellulare', 'eemail'
        , 'edocumento', 'enumero', 'evia', 'ecivico', 'ecap', 'ecomune', 'eprovincia', 'efornitore', 'epod', 'etipologia', 'epotenzaimpegnata', 'epotenzadisponibile'
        , 'eviafornitura', 'ecivicofornitura', 'ecapfornitura', 'ecomunefornitura', 'eprovinciafornitura', 'econsumoannuo', 'efornitoregas', 'epdr', 'eremi'
        , 'ematricola', 'eprontointervento', 'etipologiaduso', 'eviagas', 'ecivicogas', 'ecapgas', 'ecomunegas', 'eprovinciagas', 'econsumoannuogas', 'emodalita',
        'iban', 'eindirizzospedizione', 'eattivazione', 'epubblicita', 'esito', 'ecarica',)
    for contratti in contratta: 
        writer.writerow(contratti)

    return response
