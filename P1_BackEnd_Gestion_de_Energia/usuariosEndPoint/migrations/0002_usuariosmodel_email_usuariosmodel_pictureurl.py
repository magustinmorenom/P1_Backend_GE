# Generated by Django 5.1.2 on 2024-11-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuariosEndPoint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariosmodel',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuariosmodel',
            name='pictureurl',
            field=models.URLField(null=True),
        ),
    ]
