from django.contrib.auth import views as djviews
from django.urls import path
from parametre.forms import LoginForm
from parametre import views


context={'fichier_page_accueil': 'fichier_page_accueil.png'}

app_name="parametre"
urlpatterns = [
    path('index/', views.index, name='index'),

    path('tarification/', views.tarification, name='tarification'),
    path('composition_detail/', views.composition_detail, name='composition_detail'),
    path('composition/', views.composition, name='composition'),
    path('produit_emballage/', views.produit_emballage, name='produit_emballage'),
    path('emballage/', views.emballage, name='emballage'),
    path('produit/', views.produit, name='produit'),
    path('type_produit/', views.type_produit, name='type_produit'),
    path('fournisseur/', views.fournisseur, name='fournisseur'),
    path('machine/', views.machine, name='machine'),
    path('site/', views.site, name='site'),
    path('constructeur/', views.constructeur, name='constructeur'),

    path('commune/', views.commune, name='commune'),
    path('ville/', views.ville, name='ville'),
    path('departement/', views.departement, name='departement'),
    path('region/', views.region, name='region'),    
    path('pays/', views.pays, name='pays'),
    path('continent/', views.continent, name='continent'),
    path('societe/', views.societe, name='societe'),    

    path('login/', djviews.LoginView.as_view(template_name= 'login.html', authentication_form= LoginForm), name='login'),
    path('logout/', djviews.LogoutView.as_view(next_page='parametre:login')), 
]
