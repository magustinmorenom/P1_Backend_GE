# Generated by Django 5.1.2 on 2024-11-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suministrosEndPoint', '0002_suministromodel_nro_medidor_suministromodel_tarifa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suministromodel',
            name='tarifa',
            field=models.CharField(blank=True, choices=[('T1', 'T1'), ('T2', 'T2'), ('T3', 'T3'), ('A', 'A')], max_length=255, null=True),
        ),
    ]
