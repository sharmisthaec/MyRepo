# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortsiri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siriurl',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='siriurl',
            name='shorturl',
            field=models.CharField(default=django.utils.timezone.now, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siriurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
