# Generated by Django 4.0.5 on 2022-07-03 19:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(default=datetime.datetime(2022, 7, 3, 19, 9, 1, 934493, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
    ]
