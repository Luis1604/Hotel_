# Generated by Django 3.2.4 on 2021-06-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CajaDeAhorros', '0002_auto_20210609_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='Numero_de_Cuenta',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='transferencia',
            name='Numero_de_Cuenta',
            field=models.CharField(max_length=30),
        ),
    ]
