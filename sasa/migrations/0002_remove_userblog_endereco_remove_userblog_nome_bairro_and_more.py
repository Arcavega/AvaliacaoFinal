# Generated by Django 5.1.4 on 2024-12-16 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sasa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userblog',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='userblog',
            name='nome_bairro',
        ),
        migrations.RemoveField(
            model_name='userblog',
            name='nome_cidade',
        ),
        migrations.RemoveField(
            model_name='userblog',
            name='nome_mae',
        ),
    ]
