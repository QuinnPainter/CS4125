from django.shortcuts import render
from foodsystem_app.models.db.product import Product

class MenuView():
    current_seletected_products_ids = []

    def view_menu(request):
        products = Product.objects.all()
        return render(request, 'mainmenu.html', {'products':products})

    def add_to_order(request, id):
        MenuView.current_seletected_products_ids.append(id)
        return MenuView.view_menu(request)
    
    def remove_from_order(request, id):
        MenuView.current_seletected_products_ids.remove(id)
        return MenuView.view_menu(request)

