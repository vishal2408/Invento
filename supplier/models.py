# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=15)
    mail=models.EmailField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
    address=models.CharField(max_length=40)

    def __unicode__(self):
		return "%s" % (self.name)