# Generated by Django 5.1 on 2024-09-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portof_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='lien',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='lien',
            field=models.URLField(),
        ),
    ]
