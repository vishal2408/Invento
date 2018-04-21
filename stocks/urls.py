from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add_stock_details/', views.add_stock_details, name='add_stock_details'),
    url(r'^purchase_stock/', views.purchase_stock, name='purchase_stock'),
    url(r'^view_purchase/', views.view_purchase, name='view_purchase'),
    url(r'^view_stock_availability/', views.view_stock_availability, name='view_stock_availability'),
    url(r'^view_stock_details/', views.view_stock_details, name='view_stock_details')
]