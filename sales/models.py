# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Sales(models.Model):
    emailID=models.EmailField()
    date=models.DateField()
    billNo=models.CharField(max_length=10)
    customer=models.CharField(max_length=40)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)  #
    address=models.CharField(max_length=660)
    product=models.CharField(max_length=10)
    quantity=models.DecimalField(decimal_places=10,max_digits=14)
    rate=models.DecimalField(decimal_places=10,max_digits=14)
    avail=models.DecimalField(decimal_places=10,max_digits=14)
    total=models.DecimalField(decimal_places=10,max_digits=14)
    payment=models.DecimalField(decimal_places=10,max_digits=14)
    description=models.CharField(max_length=10)
    balance=models.DecimalField(decimal_places=10,max_digits=14)
    duedate=models.DateField()
    mode=models.CharField(max_length=10)

    def __unicode__(self):
        return "%s" % (self.customer)