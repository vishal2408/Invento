# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from purchase.models import Purchase

# Create your views here.
def purchase_stock(request):

	if request.method == 'POST':
		purchase = Purchase()
		date = request.POST.get('Date')
		billNo = request.POST.get('billNo')
		customer = request.POST.get('Customer_name')
		address =request.POST.get('Address')
		contact =request.POST.get('Contact')
		product_name = request.POST.get('Product_name')
		quantity = request.POST.get('Quantity')
		rate = request.POST.get('Rate')
		total =request.POST.get('Total')
		payment =request.POST.get('Payment')
		description = request.POST.get('Description')
		balance = request.POST.get('balance')
		mode = request.POST.get('Mode')
		purchase.save()

	return render(request, 'purchase_stock.html', {})

def view_purchase(request):
	purchase = Purchase.objects.all()
	return render(request, 'view_purchase.html', {'purchase':purchase})
