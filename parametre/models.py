# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone
from Utilitaire import *#dateAnglaisFrancais, iif, millier
from django.urls import reverse
#from multipleselectionfield import MultipleSelectionField
import datetime
from itertools import groupby
from django.shortcuts import render, get_object_or_404
import json
from django.db.models import Q, Sum, F, Avg
from datetime import date, timedelta
from django.core.exceptions import ValidationError

from dateutil.relativedelta import relativedelta


MODE_PAIEMENT = (('E','Espèces'), ('C', 'Chèque'), ('V', 'Virement'))

TYPE_CONTRAT = (
    ('Vente libre', 'Vente libre'), 
    ('Forfait', 'Forfait'),
    ('Palier', 'Palier'),
)

UNITE_MESURE = (
    ('Kg', 'Kg'), 
    ('L', 'L'),
    ('M2', 'M2'),
)

TYPE_EMBALLAGE = (
    ('Aucun', 'Aucun'),
    ('Carton', 'Carton'),
    ('Paquet', 'Paquet'),
    ('Gobelet', 'Gobelet'),
    ('Boite', 'Boite'),
    ('Sachet', 'Sachet'),
)

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class Continent(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name="Abrégé")
    
    class Meta:
        ordering=('libelle',)
    
    def __str__(self):
        return "{0}".format(self.libelle)

class Pays(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, verbose_name="Continent")
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="Abrégé")
    
    class Meta:
        ordering=('libelle',)   
    
    def __str__(self):
        return "{0}".format(self.libelle)

class Region(models.Model):
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, verbose_name="Pays")
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name="Abrégé")
    
    def __str__(self):
        return "{0}".format(self.libelle)

class Departement(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Région")
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name="Abrégé")
    
    def __str__(self):
        return "{0}".format(self.libelle)

class Ville(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, verbose_name="Département")
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name="Abrégé")
    
    def __str__(self):
        return "{0}".format(self.libelle)

class Commune(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, verbose_name="Ville")
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name="Abrégé")
    
    def __str__(self):
        return "{0}".format(self.libelle)

class Civilite(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name=u"Abrégé")

    def __str__(self):
        return "{0}".format(self.abrege)

class Fonction(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="Abrégé")
    def __str__(self):
        return "{0}".format (self.libelle)

class Profession(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True,  null=True, verbose_name=u"Libellé")

    def __str__(self):
        return "{0}".format(self.libelle)


class Canal(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name=u"Abrégé")

    def __str__(self):
        return "{0}".format(self.libelle)


class Service(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name=u"Abrégé")

    def __str__(self):
        return "{0}".format(self.libelle)

class TypeActivite(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name=u"Abrégé")

    class Meta:
        ordering=('libelle',)

    def __str__(self):
        return "{0}".format(self.libelle)

class Activite(models.Model):
    typeActivite = models.ForeignKey(TypeActivite, on_delete=models.CASCADE, verbose_name="Type d'activite")
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name=u"Abrégé")

    def __str__(self):
        return "{0}".format(self.libelle)

class Site(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="site ou client")
    sigle = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="abrégé")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    email = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="e-mail")
    contact = models.CharField(max_length=100, default='', verbose_name="contact")
    emplacement = models.CharField(max_length=100, default='', verbose_name="emplacement")
    logo = models.ImageField(upload_to='sites', blank=True, null=True, verbose_name="logo")
    photo = models.ImageField(upload_to='sites', blank=True, null=True, verbose_name="photo")

    class Meta:
        ordering = ['libelle',]

    def __str__(self):
        return "{0}".format(self.libelle)


class Profil(TimeStampModel):
    SEXES = (('M', 'Masculin'), ('F', 'Féminin'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="nom d'utilisateur") # La liaison OneToOne vers le modèle User
    civilite = models.ForeignKey(Civilite, on_delete=models.CASCADE, verbose_name="civilité")
    fonction = models.ForeignKey(Fonction,  on_delete=models.CASCADE, verbose_name="fonction")
    profession = models.ForeignKey(Profession,  on_delete=models.CASCADE, verbose_name="profession")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    email = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="e-mail")
    sexe = models.CharField(max_length=1, choices=SEXES, default='M', verbose_name="sexe")
    photo = models.ImageField(upload_to='users', blank=True, null=True, verbose_name="photo")
    
    def __str__(self):
        if self.user.first_name:
            return "{0}, {1}".format(self.user.last_name.upper()+' '+self.user.first_name.title(), self.fonction)
        else:
            return "{0}, {1}".format(self.user.last_name.upper(), self.fonction)


class Constructeur(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé")
    abrege = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name="Abrégé")
    
    def __str__(self):
        return "{0}, {1}".format(self.libelle, self.abrege)

class Machine(models.Model):
    ETAT_MACHINE = (
        ('En service', 'En service'),
        ('Disponible','Disponible'),
        ('Hors service','Hors service'),
    )
    constructeur = models.ForeignKey(Constructeur, on_delete = models.CASCADE, blank=True, null=True, verbose_name="constructeur")
    matricule = models.CharField(max_length=255, unique=True, verbose_name="matricule")
    libelle = models.CharField(max_length=50, verbose_name="libellé")
    abrege = models.CharField(max_length=50, default="", blank=True, verbose_name="abrégé")
    numero_serie = models.CharField(max_length=30, default='', blank=True, verbose_name="numéro de série")
    etat = models.CharField(max_length=15, default='En service', blank=True, choices=ETAT_MACHINE, verbose_name="état")
    photo = models.ImageField(upload_to='machines', default="", blank=True, null=True, verbose_name="photo")

    def __str__(self):
        return "{} : {}".format(self.libelle, self.matricule)


class Contact(models.Model):
    contrat = models.ForeignKey("Contrat", on_delete=models.CASCADE, verbose_name="fonction")   
    civilite = models.ForeignKey(Civilite, on_delete=models.CASCADE, verbose_name="civilité")
    fonction = models.ForeignKey(Fonction, default=1, on_delete=models.CASCADE, verbose_name="fonction")
    profession = models.ForeignKey(Profession, default=1, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, verbose_name="nom")
    prenoms = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="prénoms")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    fax = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="fax")
    email = models.EmailField(default="", blank=True, null=True, verbose_name="e-mail")
    adresse = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="adresse")

    class Meta:
        ordering=('nom',)

    def __str__(self):
        return "{0} {1}".format(self.nom.upper(), iif(self.prenoms, self.prenoms,'')).strip()


class Fournisseur(models.Model):
    civilite = models.ForeignKey(Civilite, on_delete=models.CASCADE, verbose_name="civilité")
    nom = models.CharField(max_length=255, verbose_name="nom")
    prenoms = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="prénoms")
    telephone = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="cellulaire")
    email = models.EmailField(default="", blank=True, null=True, verbose_name="e-mail")
    adresse = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="adresse")
    fax = models.CharField(max_length=20, default="", blank=True, null=True, verbose_name="fax")
    
    class Meta:
        ordering=('nom',)

    def __str__(self):
        return "{0} {1}".format(self.nom.upper(), iif(self.prenoms, self.prenoms,'')).strip()


class Depot(models.Model):
    libelle = models.CharField(max_length=100, unique=True, verbose_name="dépôt")
    sigle = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name="sigle")
    telephone = models.CharField(max_length=20, default="", null=True, blank=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", null=True, blank=True, verbose_name="cellulaire")
    contact = models.CharField(max_length=255, default="", null=True, blank=True, verbose_name="contact")
    
    class Meta:
        ordering = ('libelle', )

    def __str__(self):
      return "{0}".format(self.libelle)


class Categorie(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name=u"Libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="Abrégé")
    
    class Meta:
        ordering=('libelle',)

    def __str__(self):
        return "{0}".format(self.libelle)


class Operation(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="abrégé")
    
    class Meta:
        ordering=('libelle',)

    def __str__(self):
        return "{0}".format(self.libelle)


class Emballage(models.Model):
    type_emballage =  models.CharField(max_length=20, blank=True, choices=TYPE_EMBALLAGE, verbose_name="type emballage")
    libelle =  models.CharField(max_length=50, unique=True, blank=True, verbose_name="libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="abrégé")
        
    class Meta:
        ordering = ('libelle',)

    def __str__(self):
        return self.libelle

class UniteMesure(models.Model):
    libelle = models.CharField(max_length=50, unique=True, verbose_name="libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="abrégé")
        
    class Meta:
        ordering = ('libelle',)
    
    def __str__(self):
        return self.libelle


class TypeProduit(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="libellé")
    abrege = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="abrégé")
    
    class Meta:
        ordering=('libelle',)

    def __str__(self):
        return "{0}".format(self.libelle)


class Produit(models.Model):
    type_produit = models.ForeignKey(TypeProduit, on_delete=models.CASCADE, verbose_name="type produit")
    unitemesure = models.CharField(max_length=15, default='Kg', choices=UNITE_MESURE, blank=True, verbose_name="unité de mesure")
    libelle = models.CharField(max_length=100, unique=True, verbose_name="produit")
    prix = models.IntegerField(default=0, blank=True, verbose_name="prix")
    stocke = models.BooleanField(default=True, blank=True, verbose_name="stocké")

    class Meta:
        ordering = ['libelle']

    def __str__(self):
        return self.libelle

     
class ProduitEmballage(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="produit")
    emballage = models.ForeignKey(Emballage, on_delete=models.CASCADE, verbose_name="emballage")
    quantite_unitaire = models.FloatField(default=1, blank=True, verbose_name="quantité unitaire")
    valeur_unitaire = models.FloatField(default=1, blank=True, verbose_name="valeur unitaire")
    libelle_quantite_unitaire = models.CharField(max_length=50, default='', blank=True, verbose_name="lqu")
    libelle_valeur_unitaire = models.CharField(max_length=50, default='', blank=True, verbose_name="lvu")

    class Meta:
        ordering = ['produit']
        unique_together = (('produit', 'emballage'),)

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.produit, self.emballage, self.quantite_unitaire, self.valeur_unitaire)


class Composition(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="libellé")
    abrege = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name="abrégé")

    def __str__(self):
        return "{0}".format(self.libelle)

class Detailscomposition(models.Model):
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.SmallIntegerField(default=1, blank=True, verbose_name="quantité")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")
    
    class Meta:
        unique_together = (('composition', 'produit',))

    def __str__(self):
        return self.produit


class Contrat(TimeStampModel):
    ETAT_CONTRAT = (('En cours','En cours'), ('Suspendu', 'Suspendu'), ('Résilié', 'Résilié'))
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name="site")
    etat_contrat = models.CharField(max_length=10, default='En cours', choices=ETAT_CONTRAT,  verbose_name="etat du contrat")
    date_contrat = models.DateField(default=datetime.date.today, blank=True, verbose_name="date du contrat")
    observation = models.TextField(default="", blank=True, verbose_name="observation")
    machines = models.ManyToManyField(Machine, through='Installation', verbose_name="machines installées")

    class Meta:
        ordering=('-date_contrat',)

    def __str__(self):
        return "{0}, {1}".format(self.site, self.date_contrat)


class Installation(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date_installation = models.DateField(default=datetime.date.today, blank=True, verbose_name="date installation")
    type_contrat = models.CharField (max_length=20, default='Vente libre', choices=TYPE_CONTRAT, verbose_name="type de contrat")
    etat = models.BooleanField(default=True, blank=True, verbose_name="en service")
    observation = models.CharField(max_length=100, default="", blank=True, verbose_name="observation")
    
    class Meta:
        ordering = ('date_installation',)
        unique_together = (('contrat', 'machine', 'date_installation'),)

    def __str__(self):
        return '{0}, {1} {2}'.format(self.contrat, self.machine, self.date_installation)


class Tarification(models.Model):
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    type_contrat = models.CharField(max_length=20, blank=True, choices=TYPE_CONTRAT, verbose_name="type")
    date_tarification = models.DateField(default=datetime.date.today, blank=True, null=True, verbose_name="date tarification")
    quantite = models.SmallIntegerField(default=1000, blank=True, verbose_name="quantié")
    pu = models.SmallIntegerField(default=200, blank=True, verbose_name="prix unitaire")

    class Meta:
        unique_together = (('installation', 'type_contrat', 'date_tarification'))

    def __str__(self):
        return '{0}, {1} {2}'.format(self.installation, self.type_contrat, self.quantite)


class Appro(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_appro = models.DateField(default=datetime.date.today, blank=True, verbose_name="date")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")
    produits = models.ManyToManyField(Produit, through='Detailsappro', verbose_name="produits")

    def __str__(self):
        return  "{0}, {1}".format(self.fournisseur, dateAnglaisFrancais(self.date_appro))


class Detailsappro(models.Model):
    appro = models.ForeignKey(Appro, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.SmallIntegerField(default=1, blank=True, verbose_name="quantié")
    pu = models.SmallIntegerField(default=0, blank=True, verbose_name="prix unitaire")

    class Meta:
        unique_together = (('appro', 'produit'))

    def __str__(self):
        return  "{0}, {1}".format(self.produit, self.quantite)


class Commande(models.Model):
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    date_commande = models.DateField(default=datetime.date.today, blank=True, null=True, verbose_name="date")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")
    produits = models.ManyToManyField(Produit, through='Detailscommande', verbose_name="produits commandés")

    def __str__(self):
        return  "{0}, {1}".format(self.installation, dateAnglaisFrancais(self.date_commande))


class Detailscommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.SmallIntegerField(default=1, blank=True, verbose_name="quantié")
    pu = models.SmallIntegerField(default=0, blank=True, verbose_name="prix unitaire")

    class Meta:
        unique_together = (('commande', 'produit'))

    def __str__(self):
        return  "{0}, {1}".format(self.produit, dateAnglaisFrancais(self.quantite))


class Tasse(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name=u"Observation")

    def __str__(self):
        return "{0}, {1}".format(self.machine, self.composition)


class Consommation(models.Model):
    date_consommation = models.DateField(default=datetime.date.today, verbose_name="date")
    date_du = models.DateField(default=datetime.date.today, verbose_name="date du")
    date_au = models.DateField(default=datetime.date.today, verbose_name="date au")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")

    class Meta:
        ordering = ('-date_consommation',)

    def __str__(self):
        return "{0}, {1}, {2}".format(dateAnglaisFrancais(self.date_consommation))


class Detailsconsommation(models.Model):
    consommation = models.ForeignKey(Consommation, on_delete=models.CASCADE)
    tasse = models.ForeignKey(Tasse, on_delete=models.CASCADE)
    quantite = models.SmallIntegerField(default=1, blank=True, verbose_name="quantité")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")


class Depense(models.Model):
    date_depense = models.DateField(default=datetime.date.today, blank=True, null=True, verbose_name="date")
    modePaiement = models.CharField(max_length=1, default='E', choices=MODE_PAIEMENT,  verbose_name="mode")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")

    def __str__(self):
      return "{0}".format(self.date_depense)


class DetailsDepense(models.Model):
    depense = models.ForeignKey(Depense, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    objet = models.CharField(max_length=255, default='', blank=True, verbose_name="objet")
    quantite = models.SmallIntegerField(default=1, blank=True, verbose_name="quantite")
    pu = models.SmallIntegerField(default=1000, blank=True, verbose_name="pu")
    mode_paiement = models.CharField(max_length=1, default='C', choices=MODE_PAIEMENT,  verbose_name="mode")
    
    def __str__(self):
      return "{0}, {1}, {2}".format(self.operation, self.objet, self.mode_paiement)


class Caisse(models.Model):
    ENCAISSEMENTS = (
        ('Encaissement', 'Encaissement'),
        ('Décaissement', 'Décaissement'),
    )
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE, verbose_name="installation")
    date_operation = models.DateField(default=datetime.date.today, verbose_name="date opération")
    montant = models.IntegerField(default=0, blank=True, verbose_name="montant")
    type_operation = models.CharField(max_length=15, default='Encaissement', choices=ENCAISSEMENTS, blank=True, verbose_name="type d'opération")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")

    class Meta:
        ordering = ['-date_operation',]
        unique_together = [('installation', 'date_operation', 'type_operation')]

    def __str__(self):
        return "{}, {}, {}, {}".format(self.installation, dateAnglaisFrancais(self.date_operation), self.type_operation, self.montant)

    def get_delete_url(self):
        return reverse('reglement:delete', args=(self.pk,))


class Inventaire(models.Model):
    depot = models.ForeignKey(Depot, on_delete=models.CASCADE, verbose_name="dépôt")
    date_inventaire = models.DateField(default=datetime.date.today, verbose_name="date inventaire")
    observation = models.CharField(max_length=225, default="", blank=True, verbose_name="observation")
    produits = models.ManyToManyField(Produit, through='Detailsinventaire', verbose_name="produits inventoriés")

    class Meta:
        ordering = ['-date_inventaire',]
        unique_together = [('depot', 'date_inventaire')]

    def __str__(self):
        return "{0}, {1}".format(self.depot,self.date_inventaire)

class Detailsinventaire(models.Model):
    inventaire = models.ForeignKey(Inventaire, on_delete=models.CASCADE, verbose_name="inventaire")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="produit")
    quantite = models.IntegerField(default=0, blank=True, verbose_name="quantité")

    class Meta:
        unique_together = (('inventaire', 'produit'))

    def __str__(self):
        return "{0}, {1}".format(self.produit, self.quantite)



class Releve(models.Model):
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE, verbose_name="machine installée")
    date_releve = models.DateField(default=datetime.date.today, verbose_name="date relevé")
    periode = models.CharField(max_length=225, default='{} {}'.format(lesMois[date.today().month-1], date.today().year), blank=True, verbose_name="période")
    date_debut = models.DateField(default=datetime.date.today, blank=True, verbose_name="date début")
    date_fin = models.DateField(default=datetime.date.today, blank=True, verbose_name="date fin")
    index_anterieur = models.SmallIntegerField(default=0, blank=True, verbose_name="index antérieur")
    index_nouveau = models.SmallIntegerField(default=100, blank=True, verbose_name="index nouveau")
    test = models.SmallIntegerField(default=0, blank=True, verbose_name="test")
    remboursement = models.SmallIntegerField(default=0, blank=True, verbose_name="remboursement")
    facture = models.BooleanField(default=False, blank=True, verbose_name="Facturé")
    solde = models.BooleanField(default=False, blank=True, verbose_name="soldé")
    observation = models.CharField(max_length=255, default='', blank=True, verbose_name="observation")

    class Meta:
            ordering = ['-date_releve',]
            unique_together = (('installation', 'date_releve'))
    
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.periode, self.date_debut, self.date_fin, self.index_anterieur, self.index_nouveau)


class Facturation(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name="site")
    reference = models.CharField(max_length=255, verbose_name="référence")
    facturation_date = models.DateField(default=datetime.date.today, blank=True, verbose_name="date facture")
    periode_du_au = models.CharField(max_length=50, default='DU 01/{}/{} AU {}'.format(str(date.today().month-1).zfill(2), date.today().year, dateAnglaisFrancais(date(date.today().year, date.today().month-1, 1) + relativedelta(months=1, days=-1))), blank=True, verbose_name="période du au")
    periode = models.CharField(max_length=225, default='{} {}'.format(lesMois[date.today().month-2], date.today().year), blank=True, verbose_name="période")
    montant = models.SmallIntegerField(default=0, verbose_name="montant")
    observation = models.CharField(max_length=255, default='', blank=True, verbose_name="observation")
    releves = models.ManyToManyField(Releve)

    class Meta:
            ordering = ['-facturation_date',]

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.periode, self.site, self.reference, self.facturation_date, self.montant)


    def procedure_calcul(code_releve=None):
        dicoInfoFacturation = {}
        dictarif = {}
        dicTarification = {}

        if not code_releve:return dicoInfoFacturation
        releve_list = Releve.objects.filter(id__in = code_releve)
        for releve in releve_list:
            tarification_list = releve.installation.tarification_set.all()
            dictarif[releve] = {}
            for tarif in tarification_list:
                print("tarification des relevés = ", releve.installation.type_contrat,  tarif.type_contrat)
                if dictarif.get(releve, None):
                    dictarif[releve].update({tarif.type_contrat:tarif})
                else:
                    dictarif[releve] = {tarif.type_contrat:tarif}
        print("dictarif = ", dictarif)
        
        for releve in dictarif:
            tarif_list = dictarif.get(releve, None)
            if tarif_list:
                consommationFacturee = 0
                montantFacture = 0
                consommationFinale = releve.index_nouveau - (releve.index_anterieur + releve.test + releve.remboursement)
                print("type de contrat = ", releve.installation.type_contrat)
                print("==============================================")
                if releve.installation.type_contrat not in ('Forfait', 'Palier'):
                    consommationFacturee = consommationFinale
                    montantFacture = consommationFacturee * tarif_list.get('Vente libre', 0).pu
                    dicoInfoFacturation[releve.installation] = [releve, {'Vente libre':{'consommation': consommationFacturee, 'montant': montantFacture, 'pu':tarif_list.get('Vente libre', 0).pu }}]
                    print("dico vente libre = ", dicoInfoFacturation)
                    
                elif 'Forfait'== '{0}'.format(releve.installation.type_contrat):
                    print ('type de contrat = Forfait')
                    if consommationFinale > tarif_list.get('Forfait', 0).quantite:
                        x = consommationFinale * tarif_list.get('Forfait', 0).pu
                        y = 0
                        consommationFacturee = consommationFinale
                        montantFacture = x + y
                        
                        dicoInfoFacturation[releve.installation] = [releve, {'Forfait':{'consommation': consommationFacturee, 'montant': montantFacture, 'pu':tarif_list.get('Forfait', 0).pu }}]
                        print("forfait = ", dicoInfoFacturation)
                    else:
                        x = tarif_list.get('Forfait', 0).quantite * tarif_list.get('Forfait', 0).pu
                        consommationFacturee = tarif_list.get('Forfait', 0).quantite
                        montantFacture = x
                        
                        dicoInfoFacturation[releve.installation] = [releve, {'Forfait':{'consommation': consommationFacturee, 'montant': montantFacture, 'pu':tarif_list.get('Forfait', 0).pu }}]
                        print("forfait dico = ", dicoInfoFacturation)
                        
                elif 'Palier'== '{0}'.format(releve.installation.type_contrat):
                    print ('type de contrat = Palier', releve.installation.type_contrat)
                    m=0
                    q = consommationFinale
                    conso = consommationFinale
                    if conso <= tarif_list.get('Forfait',0).quantite:
                        consommationFacturee = q
                        montantFacture = tarif_list.get('Forfait', 0).quantite * tarif_list.get('Forfait', 0).pu
                        dicoInfoFacturation[releve.installation] = [releve, {'Forfait':{'consommation':tarif_list.get('Forfait', 0).quantite, 'pu':tarif_list.get('Forfait',0).pu, 'montant': montantFacture }}]
                        print("palier non atteint = ",dicoInfoFacturation)
                    else:
                        conso = tarif_list.get('Forfait',0).quantite
                        montant = tarif_list.get('Forfait',0).quantite * tarif_list.get('Forfait',0).pu
                        dicoInfoFacturation[releve.installation] = [releve, {'Forfait':{'consommation': conso, 'montant': montant, 'pu':tarif_list.get('Forfait',0).pu}}]
                        print("palier forfait boucle = ", dicoInfoFacturation)
                        if consommationFinale > tarif_list.get('Forfait',0).quantite:
                            conso_restante = consommationFinale - tarif_list.get('Forfait',0).quantite
                            dicoInfoFacturation[releve.installation].append([releve, {'Palier':{'consommation': conso_restante, 'montant': conso_restante * tarif_list.get('Palier',0).pu, 'pu':tarif_list.get('Palier',0).pu }}])
                            print("palier forfait + plusieurs k = ", dicoInfoFacturation)               
        
        return dicoInfoFacturation


class Reglement(models.Model):
    facturation = models.ForeignKey(Facturation, on_delete=models.CASCADE, verbose_name="facture")
    date_reglement = models.DateField(default=datetime.date.today, verbose_name="date règlement")
    montant = models.SmallIntegerField(default=0, verbose_name="montant")
    observation = models.CharField(max_length=255, default='', blank=True, verbose_name="observation")

    class Meta:
        unique_together = (('facturation', 'date_reglement'))

    def __str__(self):
        return "{}, {}, {}".format(self.facturation, self.date_reglement, self.montant)


class Paiement(models.Model):
    appro = models.ForeignKey(Appro, on_delete=models.CASCADE, verbose_name="approvisionnement")
    date_paiement = models.DateField(default=datetime.date.today, verbose_name="date paiement")
    montant = models.SmallIntegerField(default=0, verbose_name="montant")
    observation = models.CharField(max_length=255, default='', blank=True, verbose_name="observation")

    class Meta:
        unique_together = (('appro', 'date_paiement'))

    def __str__(self):
        return "{}, {}, {}".format(self.appro, self.date_paiement, self.montant)


class Exercice(models.Model):
    EXERCICES = (
    ('Exercice 2023', 'Exercice 2023'),
    ('Exercice 2022', 'Exercice 2022'),
    ('Exercice 2021', 'Exercice 2021'),
    ('Exercice 2020', 'Exercice 2020'),
    )
    
    annee = models.CharField(max_length=15, default='Exercice 2023', unique=True, choices=EXERCICES, verbose_name="exercice")
    date_debut = models.DateField(default=datetime.date.today, blank=True, verbose_name="date début")
    date_fin = models.DateField(default=datetime.date.today, blank=True, verbose_name="date fin")
    date_cloture = models.DateField(default=datetime.date.today, blank=True, verbose_name="date clôture")
    etat = models.BooleanField(default=False, blank=True, verbose_name="clôturé")

    def __str__(self):
        return "{0}".format(self.annee)


class Cloture(models.Model):
    TYPE_CLOTURE = (
    ('Trimestre 1', 'Trimestre 1'),
    ('Trimestre 2', 'Trimestre 2'),
    ('Trimestre 3', 'Trimestre 3'),
    ('Trimestre 4', 'Trimestre 4'),
    )
    
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, verbose_name="exercice comptable")
    type_cloture = models.CharField(max_length=15, default='Trimestre 1', choices=TYPE_CLOTURE, verbose_name="type de clôture")
    date_cloture = models.DateField(default=datetime.date.today, blank=True, verbose_name="date clôture")
    etat = models.BooleanField(default=False, blank=True, verbose_name="clôturé")

    class Meta:
       ordering = ('-exercice__annee', '-type_cloture')
       unique_together = (('exercice', 'type_cloture', ),)  

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.exercice, self.type_cloture, self.date_cloture, self.etat)


class Societe(models.Model):
    raisonSociale = models.CharField(max_length=255, unique=True, verbose_name="raison sociale")
    sigle = models.CharField(max_length=50, default="", blank=True,  null=True, verbose_name="sigle")
    telephone = models.CharField(max_length=20, default="", blank=True,  null=True, verbose_name="téléphone")
    cellulaire = models.CharField(max_length=20, default="", blank=True,  null=True, verbose_name="cellulaire")
    email = models.EmailField(default="", blank=True, null=True, verbose_name="e-mail")
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, verbose_name="ville")

    html_titre = models.CharField(max_length=100, default="", blank=True,  null=True, verbose_name="titre onglet navigateur")
    html_societe_long = models.CharField(max_length=100, default="", blank=True,  null=True, verbose_name="nom société long html")
    html_societe_court = models.CharField(max_length=6, default="", blank=True,  null=True, verbose_name="nom société court html")
    cellulaire1 = models.CharField(max_length=20, default="", blank=True,  null=True, verbose_name="cellulaire")
    telephone1 = models.CharField(max_length=20, default="", blank=True,  null=True, verbose_name="téléphone")
    fichier_page_accueil = models.CharField(max_length=30, default="", blank=True,  null=True, verbose_name="fichier page accueil")

    photo = models.ImageField(upload_to='images', default="", blank=True, null=True, verbose_name="photo")
    logo = models.ImageField(upload_to='images', default="", blank=True, null=True, verbose_name="logo")
    
    def __str__(self):
        return "{0}".format(self.raisonSociale)