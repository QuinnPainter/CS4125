from django.shortcuts import render
from foodsystem_app.models.db.product import Product
from foodsystem_app.models.db.order import Order
from foodsystem_app.models.db.customer import Customer
from foodsystem_app.models.db.product_queries import ProductQueries
from foodsystem_app.models.db.customer_queries import CustomerQueries
from foodsystem_app.models.menu import Menu
from foodsystem_app.models.basket import Basket

class MenuView():
    def view_menu(request):
        menu = Menu.getMenu()
        products = menu.getProducts()
        return render(request, 'mainmenu.html', {'products':products})

    def add_to_order(request, id):
        Basket.instance().addProduct(ProductQueries.get_product_by_id(id))
        return MenuView.view_menu(request)
    
    def remove_from_order(request, id):
        Basket.instance().removeProduct(ProductQueries.get_product_by_id(id))
        return MenuView.view_menu(request)

    # Not sure if its going in here or checkout but it is working
    # demo of storing order object in db that can have many products
    # and one customer/Null if none supplied
    # I am using hard coded customer obj for now
    def store_order(request):
        order = Order()
        order.completed = True
        order.paymentMethod = "Cash"
        order.discounts = 2.0
        customer = CustomerQueries.get_customer_obj(2)
        order.customer = customer
        # Save is done before add products code below for a reason
        # ie it will error out as this order object is not present
        # and order.products.add will give error
        order.save()
        for id in MenuView.current_seletected_products_ids:
            prod = ProductQueries.get_product_by_id(id)
            order.products.add(prod)
        #order.save()
        MenuView.current_seletected_products_ids.clear()
        return MenuView.view_menu(request)
