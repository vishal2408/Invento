from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add_customer_details/', views.add_customer_details, name='add_customer_details'),
    url(r'^view_customers_details/', views.view_customers_details, name='view_customers_details')
]