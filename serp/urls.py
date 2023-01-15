from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sample_request/', views.sample_request, name='sample_request'),
    


]