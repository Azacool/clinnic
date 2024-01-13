from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Purchasing, Medicines
from .serializers import CustomerSerializer, PurchasingSerializer, MedicinesSerializer
from django.http import HttpResponse

def main(request):
    return HttpResponse('Hey bro!!')

@api_view(['GET'])
def customer_purchases(request, cust_id):
    purchases = Purchasing.objects.filter(cust_id=cust_id)
    serializer = PurchasingSerializer(purchases, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customers_by_drug(request, med_category):
    customers = Customer.objects.filter(purchasing__med_id__med_category=med_category)
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def drugs_sold_on_day(request, sale_date):
    drugs_sold = Medicines.objects.filter(sales__date=sale_date)
    serializer = MedicinesSerializer(drugs_sold, many=True)
    return Response(serializer.data)
