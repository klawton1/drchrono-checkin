# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-24 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_remove_arrivedpatient_chart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrivedpatient',
            name='walk_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='arrivedpatient',
            name='appointment_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
