# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-24 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('runner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSession',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('frame_height', models.IntegerField(blank=True, null=True)),
                ('frame_width', models.IntegerField(blank=True, null=True)),
                ('bsession_logfilename', models.CharField(blank=True, max_length=1000)),
                ('all_edges_filename', models.CharField(blank=True, max_length=1000)),
                ('edge_summary_filename', models.CharField(blank=True, max_length=1000)),
                ('tac_filename', models.CharField(blank=True, max_length=1000)),
                ('whiskers_table_filename', models.CharField(blank=True, max_length=1000)),
                ('monitor_video', models.CharField(blank=True, max_length=1000)),
                ('matfile_directory', models.CharField(blank=True, max_length=1000)),
                ('fit_b2v0', models.FloatField(blank=True, null=True)),
                ('fit_b2v1', models.FloatField(blank=True, null=True)),
                ('fit_v2b0', models.FloatField(blank=True, null=True)),
                ('fit_v2b1', models.FloatField(blank=True, null=True)),
                ('param_edge_lumthresh', models.IntegerField(blank=True, null=True)),
                ('param_edge_x0', models.IntegerField(blank=True, null=True)),
                ('param_edge_x1', models.IntegerField(blank=True, null=True)),
                ('param_edge_y0', models.IntegerField(blank=True, null=True)),
                ('param_edge_y1', models.IntegerField(blank=True, null=True)),
                ('param_fol_x0', models.IntegerField(blank=True, null=True)),
                ('param_fol_x1', models.IntegerField(blank=True, null=True)),
                ('param_fol_y0', models.IntegerField(blank=True, null=True)),
                ('param_fol_y1', models.IntegerField(blank=True, null=True)),
                ('bsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runner.Session')),
            ],
        ),
    ]
