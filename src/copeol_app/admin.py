from django.contrib import admin
from .models import Camion, Commande, Fiche_analyse, Facture, Fiche_reception

# Register your models here.
admin.site.register(Commande)
admin.site.register(Camion)
admin.site.register(Fiche_analyse)
admin.site.register(Facture)
admin.site.register(Fiche_reception)