from django.contrib import admin
from .models import *

# Register your models here.

class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'niveau')
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('nom', 'certificat_pdf', 'photo')

class PortofolioAdmin(admin.ModelAdmin):
    list_display = ('lien', 'photo')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('nom_etablissement', 'formation', 'definition_de_la_formation', 'programme1', 'programme2')   

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'profession', 'a_propos_de_moi', 'cv', 'photo') 

class AddressAdmin(admin.ModelAdmin):
    list_display = ('mail', 'numero1', 'numero2', 'url')       

admin.site.register(Personne, PersonneAdmin)
admin.site.register(Competence , CompetenceAdmin)
admin.site.register(Education , EducationAdmin)
admin.site.register(Portofolio , PortofolioAdmin)
admin.site.register(Certificate , CertificateAdmin)
admin.site.register(Address, AddressAdmin)


# mot de passe c franck et le user aussi