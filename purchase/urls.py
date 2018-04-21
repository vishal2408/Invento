from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^purchase_stock/', views.purchase_stock, name='purchase_stock'),
    url(r'^view_purchase/', views.view_purchase, name='view_purchase')
]