# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class stocks(models.Model):
    emailID=models.EmailField()
    product_name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    buying_rate=models.DecimalField(decimal_places=4,max_digits=10)
    selling_rate=models.DecimalField(decimal_places=4,max_digits=10)
    suppiler_name=models.CharField(max_length=20)
    expiry_date=models.DateField