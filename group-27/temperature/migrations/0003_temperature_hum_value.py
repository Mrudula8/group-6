# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0002_auto_20170828_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='hum_value',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
    ]
