# Generated by Django 3.2.5 on 2021-08-01 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEmpleados', '0004_auto_20210801_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='responsable',
        ),
    ]
