import time
from django.shortcuts import render
from foodsystem_app.models.db.product import Product
from foodsystem_app.models.db.order import Order
from foodsystem_app.models.db.customer import Customer
from foodsystem_app.models.db.product_queries import Product_Queries
from foodsystem_app.models.db.customer_queries import Customer_Queries

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

    # Not sure if its going in here or checkout but it is working
    # demo of storing order object in db that can have many products
    # and one customer/Null if none supplied
    # I am using hard coded customer obj for now
    def store_order(request):
        order = Order()
        order.completed = True
        order.paymentMethod = "Cash"
        order.discounts = 2.0
        customer = Customer_Queries.get_customer_obj(2)
        order.customer = customer
        # Save is done before add products code below for a reason
        # ie it will error out as this order object is not present
        # and order.products.add will give error
        order.save()
        for id in MenuView.current_seletected_products_ids:
            prod = Product_Queries.get_product_by_id(id)
            order.products.add(prod)
        #order.save()
        MenuView.current_seletected_products_ids.clear()
        return MenuView.view_menu(request)
