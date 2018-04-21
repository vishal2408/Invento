# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Purchase(models.Model):
    date = models.CharField(max_length=15, default = 'Null')
    customer=models.CharField(max_length=20)
    billNo = models.CharField(max_length=10)
    product_name=models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    rate = models.CharField(max_length=10)
    total = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s" % (self.billNo)
