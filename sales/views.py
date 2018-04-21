# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def add_sales(request):
	return render(request, 'add_sales.html', {})

def view_sales(request):
	return render(request, 'view_sales.html', {})