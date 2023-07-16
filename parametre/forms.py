# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm, inlineformset_factory, formset_factory, modelformset_factory
from django.contrib.admin.widgets import AdminDateWidget
#from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from bootstrap_datepicker_plus.widgets import DatePickerInput

from django.urls import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper, AddAnotherEditSelectedWidgetWrapper

from parametre.models import *
from datetime import date, timedelta


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="User name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class SocieteForm(ModelForm):
	class Meta:
		model=Societe
		fields= '__all__'


class ContratForm(ModelForm):
    class Meta:
      model = Contrat
      exclude=("etatContrat",)


class ContactForm(forms.ModelForm):
    class Meta:
      model = Contact
      fields = "__all__"
   

class ClotureForm(ModelForm):
    exercice = forms.ModelChoiceField(empty_label=None, queryset = Exercice.objects.order_by('-annee'))
    class Meta:
        model = Cloture
        exclude = ()
        widgets = {
           'date_cloture' : DatePickerInput(options={
                          'format': 'DD/MM/YYYY',
                          'locale': "fr",
                          }),
    }

