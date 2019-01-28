# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-18 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0016_auto_20190118_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalindicator',
            name='actuals',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'Sum of collected datas achieved', max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='indicator',
            name='actuals',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'Sum of collected datas achieved', max_digits=20, null=True),
        ),
    ]