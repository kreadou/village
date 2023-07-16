from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms import modelformset_factory

from parametre.models import * 
from .forms import SocieteForm


@login_required(login_url="login/")
def index(request):
	return render(request, 'parametre/index.html')


def tarification(request):
    return 

def fournisseur(request):
    fournisseurFormSet = modelformset_factory(Fournisseur, extra=3, exclude=())
    formset = fournisseurFormSet(queryset=Fournisseur.objects.order_by('nom'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = fournisseurFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['nom']), formset):
                i.save()
            formset = fournisseurFormSet(queryset=Fournisseur.objects.order_by('nom'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/fournisseur.html', locals())
    return render(request, 'parametre/fournisseur.html', locals())

def composition_detail(request):
    detail_compositionFormSet = modelformset_factory(Detailscomposition, extra=3, exclude=())
    formset = detail_compositionFormSet(queryset=Detailscomposition.objects.order_by('produit'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = detail_compositionFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['produit']), formset):
                i.save()
            formset = detail_compositionFormSet(queryset=Detailscomposition.objects.order_by('produit'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/composition_detail.html', locals())
    return render(request, 'parametre/composition_detail.html', locals())


def composition(request):
    compositionFormSet = modelformset_factory(Composition, extra=3, exclude=())
    formset = compositionFormSet(queryset=Composition.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = compositionFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = compositionFormSet(queryset=Composition.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/composition.html', locals())
    return render(request, 'parametre/composition.html', locals())


def produit_emballage(request):
    produit_emballageFormSet = modelformset_factory(ProduitEmballage, extra=3, exclude=())
    formset = produit_emballageFormSet(queryset=ProduitEmballage.objects.order_by('produit'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = produit_emballageFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['produit']), formset):
                i.save()
            formset = produit_emballageFormSet(queryset=ProduitEmballage.objects.order_by('produit'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/produit_emballage.html', locals())
    return render(request, 'parametre/produit_emballage.html', locals())


def emballage(request):
    emballageFormSet = modelformset_factory(Emballage, extra=3, exclude=())
    formset = emballageFormSet(queryset=Emballage.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = emballageFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = emballageFormSet(queryset=Emballage.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/emballage.html', locals())
    return render(request, 'parametre/emballage.html', locals())


def produit(request):
    produitFormSet = modelformset_factory(Produit, extra=3, exclude=())
    formset = produitFormSet(queryset=Produit.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = produitFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = produitFormSet(queryset=Produit.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/produit.html', locals())
    return render(request, 'parametre/produit.html', locals())


def type_produit(request):
    type_produitFormSet = modelformset_factory(TypeProduit, extra=3, exclude=())
    formset = type_produitFormSet(queryset=TypeProduit.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = type_produitFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = type_produitFormSet(queryset=TypeProduit.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/type_produit.html', locals())
    return render(request, 'parametre/type_produit.html', locals())


def machine(request):
    machineFormSet = modelformset_factory(Machine, extra=3, exclude=())
    formset = machineFormSet(queryset=Machine.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = machineFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = machineFormSet(queryset=Machine.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/machine.html', locals())
    return render(request, 'parametre/machine.html', locals())


def site(request):
    siteFormSet = modelformset_factory(Site, extra=3, exclude=())
    formset = siteFormSet(queryset=Site.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = siteFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = siteFormSet(queryset=Site.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/site.html', locals())
    return render(request, 'parametre/site.html', locals())



def constructeur(request):
    constructeurFormSet = modelformset_factory(Constructeur, extra=3, exclude=())
    formset = constructeurFormSet(queryset=Constructeur.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = constructeurFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = constructeurFormSet(queryset=Constructeur.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/constructeur.html', locals())
    return render(request, 'parametre/constructeur.html', locals())


def pays(request):
    paysFormSet = modelformset_factory(Pays, extra=3, exclude=())
    formset = paysFormSet(queryset=Pays.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = paysFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = paysFormSet(queryset=Pays.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/pays.html', locals())
    return render(request, 'parametre/pays.html', locals())


def region(request):
    regionFormSet = modelformset_factory(Region, extra=3, exclude=())
    formset = regionFormSet(queryset=Region.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = regionFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = regionFormSet(queryset=Region.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/region.html', locals())
    return render(request, 'parametre/region.html', locals())


def departement(request):
    departementFormSet = modelformset_factory(Departement, extra=3, exclude=())
    formset = departementFormSet(queryset=Departement.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = departementFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = departementFormSet(queryset=Departement.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/departement.html', locals())
    return render(request, 'parametre/departement.html', locals())


def ville(request):
    villeFormSet = modelformset_factory(Ville, extra=3, exclude=())
    formset = villeFormSet(queryset=Ville.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label=''
    if request.method=='POST':
        formset = villeFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = villeFormSet(queryset=Ville.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label=''
            return render(request, 'parametre/ville.html', locals())
    return render(request, 'parametre/ville.html', locals())


def commune(request):
    communeFormSet = modelformset_factory(Commune, extra=3, exclude=())
    formset = communeFormSet(queryset=Commune.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label=''

    if request.method=='POST':
        formset = communeFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = communeFormSet(queryset=Commune.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label=''
                
            return render(request, 'parametre/commune.html', locals())
    return render(request, 'parametre/commune.html', locals())


def civilite(request):
    civiliteFormSet = modelformset_factory(Civilite, extra=3, exclude=())
    formset = civiliteFormSet(queryset=Civilite.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = civiliteFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = civiliteFormSet(queryset=Civilite.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/civilite.html', locals())
    return render(request, 'parametre/civilite.html', locals())


def fonction(request):
    fonctionFormSet = modelformset_factory(Fonction, extra=3, exclude=())
    formset = fonctionFormSet(queryset=Fonction.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = fonctionFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = fonctionFormSet(queryset=Fonction.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/fonction.html', locals())
    return render(request, 'parametre/fonction.html', locals())


def profession(request):
    professionFormSet = modelformset_factory(Profession, extra=3, exclude=())
    formset = professionFormSet(queryset=Profession.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = professionFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = professionFormSet(queryset=Profession.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/profession.html', locals())
    return render(request, 'parametre/profession.html', locals())


def continent(request):
    continentFormSet = modelformset_factory(Continent, extra=3, exclude=())
    formset = continentFormSet(queryset=Continent.objects.order_by('libelle'))
    for form in formset:
        for field in form.fields:form.fields[field].label='' 
    if request.method=='POST':
        formset = continentFormSet(request.POST)
        if formset.is_valid():
            for i in filter(lambda x : (x.is_valid() and x.has_changed() and x.cleaned_data['libelle']), formset):
                i.save()
            formset = continentFormSet(queryset=Continent.objects.order_by('libelle'))
            for form in formset:
                for field in form.fields:form.fields[field].label='' 
            return render(request, 'parametre/continent.html', locals())
    return render(request, 'parametre/continent.html', locals())


def societe(request):
    try:
        societe = get_object_or_404(Societe, pk=1)
    except:
        Societe.objects.create(raisonSociale='KFE-KKO').save()
        societe = get_object_or_404(Societe, pk=1)  
    if request.method=='POST':
        form = SocieteForm(request.POST, instance=societe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('parametre:index', args=[]))
        else:return render(request, 'parametre/societe.html', locals())
    else:
        form = SocieteForm(instance=societe)
        return render(request, 'parametre/societe.html', locals())





"""
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Task
from .forms import TaskForm

# Create your views here.
# Functional based view
# Create a task
# def task_create(request):
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("tasks:task_list"))
#     else:
#         form = TaskForm()
#
#     return render(request, "tasks/task_form.html", { "form": form, })
#
#
# # Retrieve task list
# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, "tasks/task_list.html", { "tasks": tasks,})
#
#
# # Retrieve a single task
# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, "tasks/task_detail.html", { "task": task, })
#
#
# # Update a single task
# def task_update(request, pk):
#     task_obj = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(instance=task_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("tasks:task_detail", args=[pk,]))
#     else:
#         form = TaskForm(instance=task_obj)
#
#     return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})
#
#
# # Delete a single task
# def task_delete(request, pk):
#     task_obj = get_object_or_404(Task, pk=pk)
#     task_obj.delete()
#     return redirect(reverse("tasks:task_list"))

# Class Based Views
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
"""