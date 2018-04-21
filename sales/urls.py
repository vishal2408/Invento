from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^add_sales/', views.add_sales, name='add_sales'),
    url(r'^view_sales/', views.view_sales, name='view_sales')
]