from django.db import models
from foodsystem_app.models.db.product_category import ProductCategory

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return self.name
