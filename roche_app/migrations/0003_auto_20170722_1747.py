# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-22 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roche_app', '0002_auto_20170720_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roche',
            name='bbr_end',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='bbr_start',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='packaging_end_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='packaging_head_pkg_signoff',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='packaging_start_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='process_order_creation_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='process_order_release_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roche',
            name='qa_release_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
