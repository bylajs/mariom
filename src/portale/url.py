"""portale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from assoluto import views
from django.conf.urls import url
from ore.views import carica,guarda,correggia,aggiorna,Cancella,orecerca,guardatutto,orecercatutto,export_ore_csv,export_oreop_csv
from profili.views import modificaprofilo 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inizio, name='inizio'),
    path('luce', views.luce, name='luce'),
    path('gas', views.gas, name='gas'),
    path('dual', views.dual, name='dual'),
    path('show',views.show, name='show'),  
    path('edit/<int:id>/', views.edit, name='edit'), 
    path('vedi/<int:id>/', views.vedi, name='vedi'),  
    path('update/<int:id>/', views.update, name='update'),  
    path('delete/<int:id>/', views.destroy, name='delete'),
    path('cerca', views.cerca, name='cerca'),
    path('orecerca', orecerca, name='orecerca'),
    path('orecercatutto', orecercatutto, name='orecercatutto'),
    path('register', views.register, name='register'),
    path('guardatutto', guardatutto, name='guardatutto'),
    path('guarda', guarda, name='guarda'), 
    path('carica', carica, name='carica'),   
    path('modificaprofilo', modificaprofilo, name='modificaprofilo'),  
    path('correggia/<int:id>/', correggia, name='correggia'),
    path('aggiorna/<int:id>/', aggiorna, name='aggiorna'),
    path('Cancella/<int:id>/', Cancella, name='Cancella'),
    path('error_404', views.error_404, name='error_404'),
    path('export/csv/', views.export_contratti_csv, name='export_contratti_csv'),
    path('export/ore/csv/', export_ore_csv, name='export_ore_csv'),
    path('export/oreop/csv/', export_oreop_csv, name='export_oreop_csv'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

