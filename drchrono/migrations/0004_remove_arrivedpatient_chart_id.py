# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0003_auto_20170822_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrivedpatient',
            name='chart_id',
        ),
    ]
