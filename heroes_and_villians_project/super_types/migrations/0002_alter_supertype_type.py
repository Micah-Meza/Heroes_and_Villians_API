# Generated by Django 4.1.5 on 2023-01-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supertype',
            name='type',
            field=models.CharField(choices=[('Hero', 'Hero'), ('Villain', 'Villain')], default=None, max_length=7),
        ),
    ]