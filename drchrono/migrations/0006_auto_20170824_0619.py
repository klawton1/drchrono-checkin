# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-24 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0005_auto_20170824_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrivedpatient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]