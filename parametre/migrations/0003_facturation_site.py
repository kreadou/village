# Generated by Django 4.1 on 2023-06-09 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0002_installation_type_contrat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturation',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parametre.site', verbose_name='site'),
            preserve_default=False,
        ),
    ]
