# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-14 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neural_sessions', '0005_auto_20171213_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='neuralsession',
            name='ain_backlight',
            field=models.IntegerField(blank=True, default=0, help_text='0-based AIN channel number of backlight signal (add to 71)', null=True),
        ),
        migrations.AddField(
            model_name='neuralsession',
            name='ain_opto',
            field=models.IntegerField(blank=True, default=1, help_text='0-based AIN channel number of opto signal (add to 71)', null=True),
        ),
        migrations.AddField(
            model_name='neuralsession',
            name='recording_number',
            field=models.IntegerField(blank=True, help_text='main recording number to analyze', null=True),
        ),
    ]
