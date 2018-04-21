from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add_stock_details/', views.add_stock_details, name='add_stock_details'),
    url(r'^view_stock_availibility/', views.view_stock_availability, name='view_stock_availability'),
    url(r'^view_stock_details/', views.view_stock_details, name='view_stock_details')
]