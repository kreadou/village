# Generated by Django 4.1 on 2023-06-10 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0015_alter_facturation_facturation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturation',
            options={},
        ),
        migrations.RemoveField(
            model_name='facturation',
            name='facturation_date',
        ),
    ]
