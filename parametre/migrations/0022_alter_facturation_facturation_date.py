# Generated by Django 4.1 on 2023-06-10 21:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0021_alter_facturation_facturation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturation',
            name='facturation_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='date facture'),
        ),
    ]
