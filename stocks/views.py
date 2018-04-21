# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def add_stock_details(request):
	return render(request, 'add_stock_details.html', {})

def purchase_stock(request):
	return render(request, 'purchase_stock.html', {})

def view_purchase(request):
	return render(request, 'view_purchase.html', {})

def view_stock_availability(request):
	return render(request, 'view_stock_availability.html', {})

def view_stock_details(request):
	return render(request, 'view_stock_details.html', {})