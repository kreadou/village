from django.contrib import admin
from parametre.models import *

admin.site.register(Civilite)
admin.site.register(Fonction)
admin.site.register(Profession)
admin.site.register(Profil)

admin.site.register(Commune)
admin.site.register(Ville)
admin.site.register(Departement)
admin.site.register(Region)
admin.site.register(Pays)
admin.site.register(Continent)
admin.site.register(Societe)

admin.site.register(Depot)

admin.site.register(Constructeur)
admin.site.register(Site)
admin.site.register(Machine)

admin.site.register(Contrat)
admin.site.register(Installation)
admin.site.register(Tarification)

admin.site.register(Appro)
admin.site.register(Detailsappro)

admin.site.register(Commande)
admin.site.register(Detailscommande)

admin.site.register(Inventaire)
admin.site.register(Detailsinventaire)

admin.site.register(Releve)
admin.site.register(Facturation)
admin.site.register(Reglement)

admin.site.register(Paiement)
admin.site.register(Caisse)
