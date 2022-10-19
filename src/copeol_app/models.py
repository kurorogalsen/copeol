from django.db import models

# Create your models here.
#from django.forms import models


class Commande(models.Model):
    poids = models.fields.IntegerField()
    lv_commande = models.fields.CharField(max_length=6)
    provenance_commande = models.fields.CharField(max_length=100)
    date_commande = models.fields.DateField()
    
    def __str__(self):
        return 'Commande ' + self.lv_commande


class Camion(models.Model):
    poids = models.fields.IntegerField()
    immatriculationulation = models.fields.CharField(max_length=20)
    nom_transporteur = models.fields.CharField(max_length=50)
    prenom_transporteur = models.fields.CharField(max_length=50)
    
    def __str__(self):
        return  'Camion ' + self.immatriculationulation


class Fiche_analyse(models.Model):
    poids = models.fields.FloatField()
    humidite = models.fields.FloatField()
    poids = models.fields.FloatField()
    impuretes = models.fields.FloatField()
    poids_net = models.fields.FloatField()
    
    def __str__(self):
        return 'Fiche analyse ' + self.id
    


class Facture(models.Model):
    prix_unitaire = models.fields.IntegerField()
    frais_livraison = models.fields.IntegerField()
    frais_dechargement = models.fields.IntegerField()
    montant_total = models.fields.IntegerField()
    date_facture = models.fields.DateField()

    def __str__(self):
        return 'Facture ' + self.id


class Fiche_reception(models.Model):
    lv_livraison = models.ForeignKey(Commande, null=True, on_delete=models.SET_NULL)
    poids_brut = models.fields.IntegerField()
    provenance_livraison = models.fields.CharField(max_length=50)
    date_livraison = models.fields.DateField()

    def __str__(self):
        return 'Fiche reception ' + self.id
