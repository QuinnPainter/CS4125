from django.shortcuts import render
from django.views import View
from foodsystem_app.models.product import Product

class MenuView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home.html', {'products':products})
