# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-18 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MostPlayed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language', to='base.Language'),
        ),
        migrations.AddField(
            model_name='mostplayed',
            name='station',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='most_played_station', to='stations.Station'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='station',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fav_station', to='stations.Station'),
        ),
    ]