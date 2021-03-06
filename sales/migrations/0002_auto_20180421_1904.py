# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='avail',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='sales',
            name='balance',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='description',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='sales',
            name='payment',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='sales',
            name='quantity',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='sales',
            name='rate',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total',
            field=models.CharField(max_length=40),
        ),
    ]
