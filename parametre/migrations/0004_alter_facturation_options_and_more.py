# Generated by Django 4.1 on 2023-06-09 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0003_facturation_site'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturation',
            options={'ordering': ['-facturation_date']},
        ),
        migrations.RenameField(
            model_name='facturation',
            old_name='date_facturation',
            new_name='facturation_date',
        ),
    ]
