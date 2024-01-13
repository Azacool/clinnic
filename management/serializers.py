from rest_framework import serializers
from .models import Customer, Medicines, Purchasing, Pharmacist, Sales

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = '__all__'

class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing
        fields = '__all__'

class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
