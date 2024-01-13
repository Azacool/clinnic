from django.db import models

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,default="Male")
    age = models.IntegerField(default=18)
    contact_add = models.CharField(max_length=90,default='Chilonzor Tumani,9A')
    cust_email = models.EmailField(default="aziztukhtasinov0404@gmail.com")
    cust_password = models.CharField(max_length=100,default="123456789")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Medicines(models.Model):
    med_id = models.AutoField(primary_key=True)
    med_category = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    description = models.TextField(default="Something was someone")
    price = models.DecimalField(max_digits=10, decimal_places=2,default=100)

    def __str__(self):
        return self.name

class Purchasing(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    med_id = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Purchase ID: {self.purchase_id}"

class Pharmacist(models.Model):
    phar_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10,default="Male")
    age = models.IntegerField(default=18)
    contact_add = models.CharField(max_length=90,default='Chilonzor Tumani,9A')
    admin_email = models.EmailField(default="atukhtasinov22@gmail.com")
    admin_password = models.CharField(max_length=70,default="njnwccn")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    phar_id = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    med_id = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    count = models.IntegerField()
    purchase_id = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sales ID: {self.sales_id}"
