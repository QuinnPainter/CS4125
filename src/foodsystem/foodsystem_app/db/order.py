from django.db import models
from foodsystem_app.db.product import Product

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    paymentMethod = models.TextField()
    discounts = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.id + ' ' + self.date
