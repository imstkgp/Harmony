# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-07 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0006_auto_20160417_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='stationId',
            field=models.IntegerField(default=0),
        ),
    ]