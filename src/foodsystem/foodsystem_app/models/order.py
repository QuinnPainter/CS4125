from django.db import models
from foodsystem_app.models.product import Product

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    #date = 0
    #completed = False
    #paymentMethod = 0
    #discounts = {}
