# Generated by Django 5.0.4 on 2024-06-05 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0002_cargos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autentication.cargos'),
        ),
    ]
