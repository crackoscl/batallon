# Generated by Django 3.2 on 2022-07-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_clubes_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubes',
            name='logo',
            field=models.URLField(default='logo', max_length=400),
        ),
    ]