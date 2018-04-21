# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from sales.models import Sales


def add_sales(request):
	if request.method == 'POST':
		customer_s= Sales()
		emailID = request.POST.get('ID')
		date = request.POST.get('Date')
		billNo = request.POST.get('Bill No.')
		customer =request.POST.get('Customer_name')
		phone_number =request.POST.get('Contact')
		address =request.POST.get('Address')
		product = request.POST.get('Product_name')
		quantity = request.POST.get('Quantity')
		rate = request.POST.get('Rate')
		avail = request.POST.get('Avail_Qty')
		total = request.POST.get('Total')
		payment = request.POST.get('Payment')
		description = request.POST.get('Description')
		balance = request.POST.get('balance')
		duedate = request.POST.get('Due_date')
		mode = request.POST.get('Mode')
		customer_s.customer=customer
		customer_s.emailID=emailID
		customer_s.billNo=billNo
		customer_s.date=date
		customer_s.phone_number=phone_number
		customer_s.address=address
		customer_s.product=product
		customer_s.quantity=quantity
		customer_s.rate=rate
		customer_s.avail=avail
		customer_s.total=total
		customer_s.payment=payment
		customer_s.description=description
		customer_s.balance=balance
		customer_s.duedate=duedate
		customer_s.mode=mode
		customer_s.save()
	return render(request, 'add_sales.html', {})

def view_sales(request):
	sales = Sales.objects.all()
	return render(request, 'view_sales.html', {'sales': sales})