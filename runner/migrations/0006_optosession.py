# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-08 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runner', '0005_auto_20161210_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptoSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(blank=True, max_length=50)),
                ('start_power', models.FloatField(blank=True, null=True)),
                ('stop_power', models.FloatField(blank=True, null=True)),
                ('wavelength', models.FloatField(blank=True, default=593.5, null=True)),
                ('target_orientation', models.CharField(blank=True, max_length=50)),
                ('fiber_diameter', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('sham', models.NullBooleanField()),
                ('behavioral_session', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='runner.Session')),
            ],
        ),
    ]
