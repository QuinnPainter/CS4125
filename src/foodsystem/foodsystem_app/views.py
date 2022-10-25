from django.shortcuts import render
from foodsystem_app.models.product import Product

def order(request):
    products = Product.objects.all()
    return render(request, 'order.html', {'products':products})
