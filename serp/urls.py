from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_request/', views.sample_request, name='sample_request'),


    # customer related urls
    path('customer/add/', views.customer_add, name='customer_add_url'),
    path('customer/<int:customer_id>/edit/', views.customer_edit, name='customer_edit_url'),
    path('customer', views.customer_list, name='customer_list_url'),
    




]