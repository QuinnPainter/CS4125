from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField()

    def __str__(self):
        return str(self.id)