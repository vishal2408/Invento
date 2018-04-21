# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from stocks.models import Stocks


def add_stock_details(request):

	if request.method == 'POST':
		customer = Stocks()
		emailid = request.POST.get('ID')
		productname = request.POST.get('product_name')
		category = request.POST.get('category')
		buyingrate = request.POST.get('buying_rate')
		sellingrate =request.POST.get('selling_rate')
		suppliername =request.POST.get('supplier_name')
		expirydate =request.POST.get('Date')
		customer.emailID = emailid
		customer.product_name = productname
		customer.category = category
		customer.buying_rate = buyingrate
		customer.selling_rate=sellingrate
		customer.suppiler_name=suppliername
		customer.expiry_date=expirydate
		customer.save()
	return render(request, 'add_stock_details.html', {})

def purchase_stock(request):
	return render(request, 'purchase_stock.html', {})

def view_purchase(request):
	return render(request, 'view_purchase.html', {})

def view_stock_availability(request):
	return render(request, 'view_stock_availability.html', {})

def view_stock_details(request):
	return render(request, 'view_stock_details.html', {})