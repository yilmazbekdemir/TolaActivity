# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0010_auto_20170629_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checklist',
            options={'ordering': ('workflowlevel2',)},
        ),
        migrations.RenameField(
            model_name='checklist',
            old_name='agreement',
            new_name='workflowlevel2',
        ),
        migrations.RemoveField(
            model_name='documentation',
            name='project',
        ),
        migrations.AddField(
            model_name='documentation',
            name='workflowlevel2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_workflowlevel2', to='workflow.WorkflowLevel2'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2',
            name='actual_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workflowlevel2',
            name='actual_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
