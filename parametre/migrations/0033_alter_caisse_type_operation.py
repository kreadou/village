# Generated by Django 4.1 on 2023-06-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0032_alter_caisse_type_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='type_operation',
            field=models.CharField(blank=True, choices=[('Encaissement', 'Encaissement'), ('Décaissement', 'Décaissement')], default='Encaissement', max_length=15, verbose_name="type d'opération"),
        ),
    ]