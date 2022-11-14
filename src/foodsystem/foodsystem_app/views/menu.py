from django.shortcuts import render
from django.views import View
from foodsystem_app.models.product import Product
from abc import ABC, abstractmethod


MENU = []
current_order = []
order_price = 0

        
class MenuItem(): #component
    #abstract function for get products
    def getproduct():
        pass
        
class MenuProduct(MenuItem): #leaf
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        MENU[name] = price

        #this has an implementaon of abstract func where all it does is return itself

        
        #burgerscategory.add(burger)
    def removeproduct(name): 
        del MENU[name]

            

class MenuCategory(MenuItem): #composite
        #all this does is call getproduct on all its child objects
        #this has a list of menu items in it
        #get product function where it just loops through the menu items
        #then calls getproduct in menuproduct on each one
        itemsList = MENU

        def getproduct():
             for x in MENU:
                return x



class Burger(MenuItem):
    def __init__(self,price):
        self.price = price

    def return_price(self):
        return self.price



MENU.append(Burger(5))

                
burger = Burger(5)
burger.return_price()



food = MenuCategory
food.getproduct()


#different approach. need to see if quinn approves
class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass

class Basket(Item):
    def __init__(self,contents):
        self.contents = contents

    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price


class Burger(Item):
    def __init__(self,price):
        self.price = price

    def return_price(self):
        return self.price

class Chicken(Item):
    def __init__(self,price):
        self.price= price

    def return_price(self):
        return self.price

basket_contents = []

basket_contents.append(Burger(5))
basket_contents.append(Chicken(7))
cart = Basket(basket_contents)




print("total price " + str(basket_contents.return_price))