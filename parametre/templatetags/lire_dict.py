from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter
def lire_dict(dictionary, key):
    return dictionary.get(key)

from Utilitaire import dateAnglaisFrancais

@register.filter
def date_francais(variable):
    return dateAnglaisFrancais(variable)

@register.filter
def flot_str(variable):
	return str(variable).replace(',', '.')

@register.filter
def index(indexable, i):
    return indexable[i]

