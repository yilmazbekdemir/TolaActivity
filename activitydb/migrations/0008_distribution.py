# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0007_auto_20160531_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribution_name', models.CharField(max_length=255)),
                ('distribution_indicator', models.CharField(max_length=255)),
                ('distribution_implementer', models.CharField(blank=True, max_length=255, null=True)),
                ('reporting_period', models.CharField(blank=True, max_length=255, null=True)),
                ('total_beneficiaries_received_input', models.IntegerField(blank=True, null=True)),
                ('distribution_location', models.CharField(blank=True, max_length=255, null=True)),
                ('input_type_distributed', models.CharField(blank=True, max_length=255, null=True)),
                ('distributor_name_and_affiliation', models.CharField(blank=True, max_length=255, null=True)),
                ('distributor_contact_number', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('form_filled_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by_position', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_date', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_by_position', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_by_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('form_verified_date', models.CharField(blank=True, max_length=255, null=True)),
                ('total_received_input', models.CharField(blank=True, max_length=255, null=True)),
                ('total_male', models.IntegerField(blank=True, null=True)),
                ('total_female', models.IntegerField(blank=True, null=True)),
                ('total_age_0_14_male', models.IntegerField(blank=True, null=True)),
                ('total_age_0_14_female', models.IntegerField(blank=True, null=True)),
                ('total_age_15_24_male', models.IntegerField(blank=True, null=True)),
                ('total_age_15_24_female', models.IntegerField(blank=True, null=True)),
                ('total_age_25_59_male', models.IntegerField(blank=True, null=True)),
                ('total_age_25_59_female', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('activity_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.ProjectAgreement', verbose_name='Project Initiation')),
                ('office_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.Office')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.Program')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activitydb.Province')),
            ],
            options={
                'ordering': ('distribution_name',),
            },
        ),
    ]