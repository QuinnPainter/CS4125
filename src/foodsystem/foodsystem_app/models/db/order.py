from django.db import models
from foodsystem_app.models.db.product import Product
from foodsystem_app.models.db.customer import Customer

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    # if a customer is deleted we don't want this order to delete as well hence
    # replace it with NULL value if selected customer is deleted in future
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    paymentMethod = models.TextField()
    discounts = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        id_details = "Order ID = " + str(self.id)
        if(self.completed):
            completion_status = " Completed = Yes"
        else:
            completion_status = " Completed = NO"
        return id_details + completion_status
