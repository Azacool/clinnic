from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('customer_purchases/<int:cust_id>/', views.customer_purchases),
    path('customers_by_drug/<str:med_category>/', views.customers_by_drug),
    path('drugs_sold_on_day/<str:sale_date>/', views.drugs_sold_on_day),
]
