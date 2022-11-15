from django.shortcuts import render
from django.views import View
from foodsystem_app.db.product import Product

class MenuView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'mainmenu.html', {'products':products})
