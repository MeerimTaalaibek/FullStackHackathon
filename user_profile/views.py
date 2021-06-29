from rest_framework import generics

from .serializer import *


class ProfileProducerListView(generics.ListAPIView):
    queryset = ProducerProfile.objects.all()
    serializer_class = ProfileProducerSerializer

class ProfileProducerDetailView(generics.RetrieveAPIView):
    queryset = ProducerProfile.objects.all()
    serializer_class = ProfileProducerSerializer

class ProfileProducerUpdateView(generics.UpdateAPIView):
    queryset = ProducerProfile.objects.all()
    serializer_class = ProfileProducerSerializer



class ProfileCustomerListView(generics.ListAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = ProfileCustomerSerializer

class ProfileCustomerDetailView(generics.RetrieveAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = ProfileCustomerSerializer

class ProfileCustomerUpdateView(generics.UpdateAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = ProfileCustomerSerializer

