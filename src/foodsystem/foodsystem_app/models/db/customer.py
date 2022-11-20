from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    emailAddress = models.EmailField(max_length = 254)

    def __str__(self):
        return str(self.id)