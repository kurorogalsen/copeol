# Generated by Django 4.1.2 on 2022-10-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poids', models.IntegerField()),
                ('immatriculationulation', models.CharField(max_length=20)),
                ('nom_transporteur', models.CharField(max_length=50)),
                ('prenom_transporteur', models.CharField(max_length=50)),
                ('lv_livraison', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poids', models.IntegerField()),
                ('lv_commande', models.CharField(max_length=6)),
                ('provenance_commande', models.CharField(max_length=100)),
                ('date_commande', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Echantillon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidite', models.FloatField()),
                ('poids', models.FloatField()),
                ('impuretes', models.FloatField()),
                ('poids_net', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_unitaire', models.IntegerField()),
                ('frais_livraison', models.IntegerField()),
                ('frais_dechargement', models.IntegerField()),
                ('montant_total', models.IntegerField()),
                ('date_facture', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poids_brut', models.IntegerField()),
                ('provenance_livraison', models.CharField(max_length=50)),
                ('date_livraison', models.DateField()),
            ],
        ),
    ]