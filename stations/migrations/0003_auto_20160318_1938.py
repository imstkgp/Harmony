# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-18 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20160318_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='country_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='country_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='region',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
