from datetime import datetime
from django.db import models

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    a_propos_de_moi = models.TextField()
    cv = models.FileField(upload_to='cv/%Y/%m/%d/')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.nom
    
class Competence(models.Model):
    nom = models.CharField(max_length=50)
    niveau = models.IntegerField()

    def __str__(self):
        return self.nom
    
class Education(models.Model):
    nom_etablissement = models.CharField(max_length=150)
    formation = models.CharField(max_length=150)   
    definition_de_la_formation = models.CharField(max_length=150)
    programme1 = models.CharField(max_length=150)
    programme2 = models.CharField(max_length=150)
    annee_debut = models.IntegerField(default=datetime.now().year)
    annee_fin = models.IntegerField(default=datetime.now().year)
    def __str__(self):
        return self.nom_etablissement
    
class Portofolio(models.Model):
    lien = models.URLField()  
    photo = models.FileField(upload_to='photos/%Y/%m/%d' , null=True , blank=True)   

    def __str__(self):
        return self.lien


class Certificate(models.Model):
    nom = models.CharField(max_length=50)
    certificat_pdf= models.FileField(upload_to='photos/%Y/%m/%d' , null=True , blank=True)
    photo = models.FileField(upload_to='photos/%Y/%m/%d' , null=True , blank=True)

    def __str__(self):
        return self.nom
    
class Address (models.Model):
    mail = models.EmailField()
    numero1 = models.CharField(max_length=50)
    numero2 = models.CharField(max_length=50)
    url = models.URLField()   

    def __str__(self):
        return self.mail