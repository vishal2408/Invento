# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def add_customer_details(request):
	return render(request, 'add_customer_details.html', {})

def view_customers_details(request):
	return render(request, 'view_customers_details.html', {})