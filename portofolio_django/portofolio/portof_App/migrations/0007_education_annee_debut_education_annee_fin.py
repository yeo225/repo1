# Generated by Django 5.1 on 2024-09-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portof_App', '0006_alter_personne_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='annee_debut',
            field=models.IntegerField(default=2024),
        ),
        migrations.AddField(
            model_name='education',
            name='annee_fin',
            field=models.IntegerField(default=2024),
        ),
    ]