# Generated by Django 4.0.4 on 2022-05-29 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_cadeira_linguagens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tecnologia',
            name='logo',
        ),
    ]