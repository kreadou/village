# Generated by Django 4.1 on 2023-06-10 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0008_alter_facturation_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturation',
            old_name='facturation_numero',
            new_name='periode_du_au',
        ),
    ]