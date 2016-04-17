# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_station_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='categoryDescription',
            new_name='genre_description',
        ),
        migrations.RenameField(
            model_name='station',
            old_name='categoryId',
            new_name='genre_id',
        ),
        migrations.RenameField(
            model_name='station',
            old_name='categoryTitle',
            new_name='genre_name',
        ),
    ]