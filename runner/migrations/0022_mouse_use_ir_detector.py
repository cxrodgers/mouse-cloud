# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-10 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runner', '0021_auto_20170505_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouse',
            name='use_ir_detector',
            field=models.NullBooleanField(),
        ),
    ]