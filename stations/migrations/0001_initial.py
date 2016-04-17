# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('country_code', models.CharField(max_length=50)),
                ('country_name', models.CharField(max_length=300)),
                ('region', models.CharField(max_length=300)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('thumb_url', models.URLField(blank=True, max_length=500, null=True)),
                ('stream_url', models.URLField(blank=True, max_length=500, null=True)),
                ('website', models.CharField(blank=True, max_length=500, null=True)),
                ('stationId', models.IntegerField(default=0)),
                ('categoryId', models.IntegerField(default=0)),
                ('categoryTitle', models.CharField(blank=True, max_length=300, null=True)),
                ('categoryDescription', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
