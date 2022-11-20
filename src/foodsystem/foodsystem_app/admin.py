from django.contrib import admin
from foodsystem_app.models.db.customer import Customer
from foodsystem_app.models.db.product import Product
from foodsystem_app.models.db.employee import Employee
from foodsystem_app.models.db.order import Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Order)