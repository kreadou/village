# Generated by Django 4.1 on 2023-06-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0031_rename_date_opération_caisse_date_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='type_operation',
            field=models.BooleanField(blank=True, default=True, verbose_name='encaissement'),
        ),
    ]