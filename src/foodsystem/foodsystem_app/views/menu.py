from django.shortcuts import render
from django.views import View
from foodsystem_app.models.product import Product
from abc import abstractmethod


MENU = {}
current_order = []
order_price = 0

        
class MenuItem(): #component
    #abstract function for get products
    def getproduct():
        return
        
class MenuProduct(MenuItem): #leaf
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        MENU[name] = price

        #this has an implementaon of abstract func where all it does is return itself

        burger = MenuProduct()
        #burgerscategory.add(burger)
        def getproduct(): 
            print("Product:")
            print(self)
            return self

class MenuCategory(MenuItem): #composite
        #all this does is call getproduct on all its child objects
        #this has a list of menu items in it
        #get product function where it just loops through the menu items
        #then calls getproduct in menuproduct on each one
        itemsList = MENU

        def getproduct():
             for x in MENU:
                return x
                
    

