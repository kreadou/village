# Generated by Django 4.1 on 2023-06-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0020_alter_facturation_facturation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturation',
            name='facturation_date',
            field=models.DateField(auto_now=True, verbose_name='date facture'),
        ),
    ]