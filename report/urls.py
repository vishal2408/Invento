from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^sales_product/', views.sales_product, name='sales_product'),
    url(r'^profit_report/', views.profit_report, name='profit_report')
]