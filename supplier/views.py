# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from supplier.models import Supplier


def add_supplier_details(request):

	if request.method == 'POST':
		customer = Supplier()
		name = request.POST.get('name')
		mail = request.POST.get('email')
		phone_number = request.POST.get('contact')
		address = request.POST.get('comment')
		customer.name = name
		customer.mail = mail
		customer.phone_number = phone_number
		customer.address = address
		customer.save()
	return render(request, 'add_supplier_details.html',{})

def view_suppliers_details(request):
	supplier = Supplier.objects.all()
	return render(request, 'view_suppliers_details.html', {'supplier':supplier})