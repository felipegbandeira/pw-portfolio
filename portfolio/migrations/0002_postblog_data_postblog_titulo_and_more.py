# Generated by Django 4.0.4 on 2022-05-22 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postblog',
            name='titulo',
            field=models.CharField(default='titulo', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postblog',
            name='comentario',
            field=models.CharField(max_length=450),
        ),
    ]
