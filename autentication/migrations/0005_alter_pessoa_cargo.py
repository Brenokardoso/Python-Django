# Generated by Django 5.0.4 on 2024-06-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0004_remove_pessoa_cargo_pessoa_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cargo',
            field=models.ManyToManyField(blank=True, to='autentication.cargos', verbose_name='Cargos'),
        ),
    ]