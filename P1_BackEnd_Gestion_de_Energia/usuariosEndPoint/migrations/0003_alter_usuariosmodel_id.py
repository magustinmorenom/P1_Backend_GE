# Generated by Django 5.1.2 on 2024-11-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuariosEndPoint', '0002_usuariosmodel_email_usuariosmodel_pictureurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariosmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
