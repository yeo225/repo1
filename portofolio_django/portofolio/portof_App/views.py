from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.

def index(request , id=1):
    competences = Competence.objects.all()
    education = Education.objects.all()
    portofolio = Portofolio.objects.all()
    certificate = Certificate.objects.all()
    personne = get_object_or_404(Personne, id=id)
    adress_users = Address.objects.all()
    return render(request, 'site/index.html', {'competences':competences, 'educations':education, 'portofolios':portofolio, 'certificates':certificate, 'personne':personne , 'adressUsers':adress_users})
