# Generated by Django 5.1 on 2024-09-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portof_App', '0003_alter_certificate_photo_alter_personne_cv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='photo',
            field=models.FileField(upload_to='doc/%Y/%m/%d '),
        ),
    ]