# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-21 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailID', models.EmailField(max_length=254)),
                ('product_name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('buying_rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('selling_rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('suppiler_name', models.CharField(max_length=20)),
            ],
        ),
    ]
