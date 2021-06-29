from django.urls import path
from .views import *

urlpatterns = [
    path('producer/', ProfileProducerListView.as_view()),
    path('producer/<int:pk>/', ProfileProducerDetailView.as_view()),
    path('producer-update/<int:pk>/', ProfileProducerUpdateView.as_view()),
    path('customer/', ProfileCustomerListView.as_view()),
    path('customer/<int:pk>/', ProfileCustomerDetailView.as_view()),
    path('customer-update/<int:pk>/', ProfileCustomerUpdateView.as_view()),
]