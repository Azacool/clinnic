from django.contrib import admin
from .models import Customer, Medicines, Purchasing, Sales,Pharmacist

admin.site.register(Customer)
admin.site.register(Medicines)
admin.site.register(Purchasing)
admin.site.register(Sales)
admin.site.register(Pharmacist)
