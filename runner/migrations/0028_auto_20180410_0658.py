# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-10 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runner', '0027_mouse_experimenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='experimenter',
            field=models.IntegerField(choices=[(0, 'chris'), (1, 'jung')], default=0),
            preserve_default=False,
        ),
    ]
