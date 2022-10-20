import datetime
from django.db import models

# Create your models here.
#from django.forms import models


class Commande(models.Model):
    lv_commande = models.fields.CharField(max_length=6)
    provenance_commande = models.fields.CharField(max_length=100)
    date_commande = models.fields.DateField()

    def __str__(self):
        return 'Commande ' + self.lv_commande


class Fiche_reception(models.Model):
    lv_livraison = models.ForeignKey(Commande,
                                     null=True,
                                     on_delete=models.SET_NULL)
    poids_brut = models.fields.IntegerField()
    provenance_livraison = models.fields.CharField(max_length=50)
    date_livraison = models.fields.DateField()

    def __str__(self):
        return 'Fiche reception ' + self.lv_livraison.lv_commande


class Fiche_analyse(models.Model):
    VARIETE1 = 'Décortiquées'
    VARIETE2 = 'Coques'

    CHOICES = (
        (VARIETE1, 'Décortiquées'),
        (VARIETE2, 'Coques'),
    )

    variete = models.CharField(max_length=15, choices=CHOICES)
    fiche_reception = models.ForeignKey(Fiche_reception,
                                        null=True,
                                        on_delete=models.SET_NULL)
    humidite = models.fields.FloatField()
    impuretes = models.fields.FloatField()
    taux_graines_defectueuses = models.fields.IntegerField()

    def __str__(self):
        return 'Fiche analyse ' + self.id


class Facture(models.Model):
    fiche_analyse = models.fields.CharField(max_length=100)
    provenance = models.fields.CharField(max_length=100)
    pnc = models.fields.FloatField()
    prix_unitaire = models.fields.IntegerField(default=0)
    frais_livraison = models.fields.IntegerField(default=0)
    frais_dechargement = models.fields.IntegerField(default=0)
    montant_total = models.fields.IntegerField(default=0)
    date_facture = models.fields.DateField()
    #dater = datetime.today()

    def __str__(self):
        return 'Facture ' + self.id