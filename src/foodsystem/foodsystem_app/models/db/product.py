from django.models.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name