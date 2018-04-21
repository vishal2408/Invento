# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def sales_product(request):
	return render(request, 'sales_product.html', {})

def profit_report(request):
	return render(request, 'profit_report.html', {})