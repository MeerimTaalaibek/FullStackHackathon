from rest_framework import serializers
from .models import *

class ProfileProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerProfile
        fields = '__all__'

class ProfileCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'