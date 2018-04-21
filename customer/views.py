# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from customer.models import Customer

# Create your views here.
def add_customer_details(request):
	
	if request.method == 'POST':
		customer = Customer()
		name = request.POST.get('name')
		mail = request.POST.get('email')
		phone_number = request.POST.get('contact')
		address = request.POST.get('comment')
		customer.name = name
		customer.mail = mail
		customer.phone_number = phone_number
		customer.address = address
		customer.save()
	return render(request, 'add_customer_details.html', {})

def view_customers_details(request):
	return render(request, 'view_customers_details.html', {})