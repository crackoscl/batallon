# Generated by Django 3.2 on 2022-07-18 00:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_clubes_imagen_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', ckeditor.fields.RichTextField(default='aqui texto')),
                ('fecha', models.DateField()),
                ('link_evento', models.CharField(max_length=400)),
            ],
        ),
    ]
