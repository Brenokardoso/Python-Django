# Generated by Django 5.0.4 on 2024-06-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do cargo')),
                ('lotacao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lotação')),
            ],
        ),
    ]
