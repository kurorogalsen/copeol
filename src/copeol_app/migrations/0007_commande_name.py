# Generated by Django 4.1.2 on 2022-10-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copeol_app', '0006_fiche_reception_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='name',
            field=models.CharField(default=models.CharField(max_length=6), editable=False, max_length=100),
        ),
    ]
