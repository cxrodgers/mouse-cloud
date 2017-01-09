# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-09 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runner', '0009_auto_20170109_1245'),
        ('neural_sessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neuralsession',
            name='grand_session',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='runner.GrandSession'),
        ),
    ]