# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def add_supplier_details(request):
	return render(request, 'add_supplier_details.html', {})

def view_suppliers_details(request):
	return render(request, 'view_suppliers_details.html', {})