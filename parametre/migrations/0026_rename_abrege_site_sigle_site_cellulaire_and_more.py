# Generated by Django 4.1 on 2023-06-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametre', '0025_alter_facturation_periode_du_au'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='abrege',
            new_name='sigle',
        ),
        migrations.AddField(
            model_name='site',
            name='cellulaire',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='cellulaire'),
        ),
        migrations.AddField(
            model_name='site',
            name='contact',
            field=models.CharField(default='', max_length=100, verbose_name='contact'),
        ),
        migrations.AddField(
            model_name='site',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='e-mail'),
        ),
        migrations.AddField(
            model_name='site',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='sites', verbose_name='logo'),
        ),
        migrations.AddField(
            model_name='site',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='sites', verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='site',
            name='telephone',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='téléphone'),
        ),
    ]
