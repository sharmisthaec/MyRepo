# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import shortsiri.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortsiri', '0003_siriurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siriurl',
            name='address',
            field=models.CharField(max_length=200, validators=[shortsiri.validators.validate_url, shortsiri.validators.validate_dot_com]),
        ),
    ]
