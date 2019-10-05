from django.shortcuts import render 
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import When, F, Q
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from django.db.models import IntegerField, F, Case, When
from django.db.models.functions import Coalesce
from django.db.models import Value
from django.db.models import  Case
from .models import Ore
from .forms import CreateNewOre, CreateNewOreupdate
from datetime import timedelta
from django.utils import timezone
import datetime
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.functions import Coalesce
import csv
  
 

# Create your views here.
#formi per te caricuar Oret dhe Contrattat
@login_required(login_url='/login/') 
def carica(request):
    if not request.user.is_staff:
       return redirect('/error_404')  
    if request.method == "POST":  
        form = CreateNewOre(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                messages.success(request, 'I dati sono stati inseriti con successo.')
                return redirect('/carica')  
            except:  
                pass  
    else:  
        form = CreateNewOre()  
    return render(request,'carica.html',{'form':form}) 
@login_required(login_url='/login/')
@permission_required('ore.is_operatore', raise_exception=True)
#faqa qe shikon operatori
def guarda(request):
    ore = Ore.objects.all()
    ore_list = Ore.objects.filter(user=request.user)
    sum = Ore.objects.filter(user=request.user).aggregate(totals=Coalesce(Sum('oret'), (0)))
    contratti = Ore.objects.filter(user=request.user).aggregate(totals=Coalesce(Sum('contrattiok'), (0)))
    contrattiko = Ore.objects.filter(user=request.user).aggregate(totals=Coalesce(Sum('contrattiko'), (0)))
    this_month = datetime.now().month
    oret = Ore.objects.filter(user=request.user,data__month=this_month).aggregate(totals=Coalesce(Sum("oret"), (0)))
    ok = Ore.objects.filter(user=request.user,data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiok"), (0)))
    ko = Ore.objects.filter(user=request.user,data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiko"), (0)))
    qcok = Ore.objects.filter(user=request.user,statuse='Check Call Ok',data__month=this_month).count()
    page = request.GET.get('page', 1)

    paginator = Paginator(ore_list, 10)
    try:
        ore = paginator.page(page)
    except PageNotAnInteger:
        ore = paginator.page(1)
    except EmptyPage:
        ore = paginator.page(paginator.num_pages)
    return render(request,"guarda.html",{'ore':ore,'qcok':qcok,'oret':oret,'ok':ok,'ko':ko,'sum':sum,'contratti':contratti,'contrattiko':contrattiko})
#faqa qe shikon supervizori
@login_required(login_url='/login/') 
def guardatutto(request):
    if not request.user.is_staff:
       return redirect('/error_404')
    ore = Ore.objects.all()
    ore_list = Ore.objects.filter()
    sum = Ore.objects.filter().aggregate(totals=Coalesce(Sum('oret'), (0)))
    contratti = Ore.objects.filter().aggregate(totals=Coalesce(Sum('contrattiok'), (0)))
    contrattiko = Ore.objects.filter().aggregate(totals=Coalesce(Sum('contrattiko'), (0)))
    this_month = datetime.now().month
    orettutto = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("oret"), (0)))
    oktutto = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiok"), (0)))
    kotutto = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiko"), (0)))
    qcoktutto = Ore.objects.filter(statuse='Check Call Ok',data__month=this_month).count()
    page = request.GET.get('page', 1)

    paginator = Paginator(ore_list, 8)
    try:
        ore = paginator.page(page)
    except PageNotAnInteger:
        ore = paginator.page(1)
    except EmptyPage:
        ore = paginator.page(paginator.num_pages)
    return render(request,"guardatutto.html",{'ore':ore,'qcoktutto':qcoktutto,'orettutto':orettutto,'oktutto':oktutto,'kotutto':kotutto,'sum':sum,'contratti':contratti,'contrattiko':contrattiko})
#azioni per te modifikuar objektin
@login_required(login_url='/login/') 
def correggia(request, id):
    if not request.user.is_staff:
       return redirect('/error_404')  
    ore = Ore.objects.get(id=id)  
    return render(request,'correggia.html', {'ore':ore})  
#azioni per te aggiornuar objektin
@login_required(login_url='/login/') 
def aggiorna(request, id):
    if not request.user.is_staff:
       return redirect('/error_404')  
    ore = Ore.objects.get(id=id)  
    form = CreateNewOreupdate(request.POST, instance = ore,)  
    if form.is_valid():
        form.save()
        messages.success(request, 'Scheda Aggiornata con successo.')
        return redirect("/guardatutto")  
    return render(request, 'correggia.html', {'ore': ore,}) 
#azioni per te fshir objektin 
@login_required(login_url='/login/') 
def Cancella(request, id):
    if not request.user.is_staff:
       return redirect('/error_404')
    ore = Ore.objects.get(id=id)
    if request.method == "POST":
        ore.delete()
        messages.success(request, 'Scheda Cancellata con successo.')
        return redirect('/guardatutto')
    context = {
        "ore": ore
    }
    return render(request, "scheda-cancellata.html", context)
#formi per te kerkuar per operatorin  
def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required(login_url='/login/')
@permission_required('ore.is_operatore')
def orecerca(request):
    qs = Ore.objects.filter(user=request.user)
    this_month = datetime.now().month
    oret = Ore.objects.filter(user=request.user,data__month=this_month).aggregate(totals=Coalesce(Sum("oret"), (0)))
    ok = Ore.objects.filter(user=request.user,data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiok"), (0)))
    ko = Ore.objects.filter(user=request.user,data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiko"), (0)))
    qcok = Ore.objects.filter(user=request.user,statuse='Check Call Ok',data__month=this_month).count()
    statuse = request.GET.get('statuse')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if is_valid_queryparam(statuse):
        qs = qs.filter(statuse=statuse)

    if is_valid_queryparam(date_min):
        qs = qs.filter(data__gte=date_min) 

    if is_valid_queryparam(date_max): 
        qs = qs.filter(data__lte=date_max)

    total = qs.aggregate(totals=Coalesce(Sum('oret'), (0)))
    contratti = qs.aggregate(totals=Coalesce(Sum('contrattiok'), (0)))
    contrattiko = qs.aggregate(totals=Coalesce(Sum('contrattiko'), (0)))

    context = {
        'ore': qs,
        'sum': total,
        'contratti': contratti,
        'contrattiko': contrattiko,
        'oret':oret,
        'ok':ok,
        'ko':ko,
        'qcok':qcok,
    } 
    return render(request, "guarda.html", context,)
#formi per te kerkuar per supervizorin    
@login_required(login_url='/login/') 
def orecercatutto(request):
    if not request.user.is_staff:
       return redirect('/error_404')
    qs = Ore.objects.filter()
    this_month = datetime.now().month
    orettutto = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("oret"), (0)))
    oktutto = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiok"), (0)))
    kotutto = Ore.objects.filter(data__month=this_month).aggregate(totals=Coalesce(Sum("contrattiko"), (0)))
    qcoktutto = Ore.objects.filter(statuse='Check Call Ok').count()
    statuse = request.GET.get('statuse')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if is_valid_queryparam(statuse):
        qs = qs.filter(statuse=statuse)

    if is_valid_queryparam(date_min):
        qs = qs.filter(data__gte=date_min) 

    if is_valid_queryparam(date_max): 
        qs = qs.filter(data__lte=date_max)

    total = qs.aggregate(totals=Coalesce(Sum('oret'), (0)))
    contratti = qs.aggregate(totals=Coalesce(Sum('contrattiok'), (0)))
    contrattiko = qs.aggregate(totals=Coalesce(Sum('contrattiko'), (0)))

    context = {
        'ore': qs,
        'sum': total,
        'contratti': contratti,
        'contrattiko': contrattiko,
        'orettutto':orettutto,
        'oktutto':oktutto,
        'kotutto':kotutto,
        'qcoktutto':qcoktutto,
    } 
    return render(request, "guardatutto.html", context,) 


@login_required(login_url='/login/') 
def export_ore_csv(request):
    if not request.user.is_staff:
       return redirect('/error_404')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ore.csv"'

    writer = csv.writer(response)
    writer.writerow(['user_id', 'data', 'oret', 'contrattiok', 'contrattiko', 'statuse',])

    ore = Ore.objects.all().values_list('user_id', 'data', 'oret', 'contrattiok', 'contrattiko', 'statuse',)
    for ore in ore: 
        writer.writerow(ore)

    return response

@login_required(login_url='/login/') 
@permission_required('ore.is_operatore', raise_exception=True)
def export_oreop_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ore.csv"'

    writer = csv.writer(response)
    writer.writerow(['user_id', 'data', 'oret', 'contrattiok', 'contrattiko', 'statuse',])

    ore = Ore.objects.filter(user=request.user).values_list('user_id', 'data', 'oret', 'contrattiok', 'contrattiko', 'statuse',)
    for ore in ore: 
        writer.writerow(ore)

    return response
