from django.db import models
from .customer import Customer
from .product import Product
import datetime


        


class Order(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity  = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=100,default='',blank=True)
    zone  = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=12,default='',blank=True)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
        
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)


