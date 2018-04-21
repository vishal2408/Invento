from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add_supplier_details/', views.add_supplier_details, name='add_supplier_details'),
    url(r'^view_suppliers_details/', views.view_suppliers_details, name='view_suppliers_details')
]