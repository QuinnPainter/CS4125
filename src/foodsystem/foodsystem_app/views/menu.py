from django.shortcuts import render
from foodsystem_app.db.product import Product

class MenuView():
    def view_menu(request):
        products = Product.objects.all()
        return render(request, 'mainmenu.html', {'products':products})

    def add_to_order(request, id):
        # Add product with id into basket
        print(id)
        return MenuView.view_menu(request)
