# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-09 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0009_auto_20180109_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='public_all',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='public_in_org',
            field=models.BooleanField(default=0),
        ),
    ]
