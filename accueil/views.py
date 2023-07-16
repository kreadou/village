from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required, login_required

from parametre.models import Societe

@login_required(login_url="login/")
def index(request):
	societe = get_object_or_404(Societe, pk=1)
	return render(request, 'accueil/index.html', context={'societe':societe})
