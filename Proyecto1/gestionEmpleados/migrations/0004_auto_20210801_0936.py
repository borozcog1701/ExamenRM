# Generated by Django 3.2.5 on 2021-08-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEmpleados', '0003_auto_20210731_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='responsable',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='contacto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='direccion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
