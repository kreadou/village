# Generated by Django 4.1 on 2023-06-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0011_alter_facturation_periode_du_au'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturation',
            name='periode_du_au',
            field=models.CharField(blank=True, default='DU 01/5/2023 AU 31/05/2023', max_length=50, verbose_name='période du au'),
        ),
    ]
