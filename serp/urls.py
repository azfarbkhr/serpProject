from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_request/', views.sample_request, name='sample_request'),

    # customer related urls
    path('customer/add/', views.customer_add, name='customer_add_url'),
    path('customer/<int:customer_id>/edit/', views.customer_edit, name='customer_edit_url'),
    path('customer', views.customer_list, name='customer_list_url'),

    # consultations related urls
    path('consultation/add/', views.consultation_add, name='consultation_add_url'),
    path('consultation/<int:consultation_id>/edit/', views.consultation_edit, name='consultation_edit_url'),
    path('consultation', views.consultation_list, name='consultation_list_url'),    

    # invoice related urls
    path('invoice/add/', views.invoice_add, name='invoice_add_url'),
    path('invoice/<int:invoice_id>/edit/', views.invoice_edit, name='invoice_edit_url'),
    path('invoice', views.invoice_list, name='invoice_list_url'),



]