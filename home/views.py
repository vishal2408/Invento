# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
	return render(request, 'welcome.html', {})

def dashboard(request):
	return render(request, 'index.html', {})


class HomeView(View):
	home = 'welcome.html'
	index = 'index.html'
	login = 'login.html'
	form_class = LoginForm
	initial = {'key' : 'value'}

	def get(self, request):
		form = self.form_class(request.POST)
		return render(request, self.login, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.cleaned_data.get('user')
			password = form.cleaned_data.get('password')

			if user == 'admin' and password == 'admin':
				return HttpResponseRedirect('/dashboard/')
				# return render(request, self.index, {})
			else:
				return render(request, self.home, {})	

