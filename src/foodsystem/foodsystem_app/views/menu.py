from django.shortcuts import render
from foodsystem_app.db.product import Product
from abc import abstractmethod, ABC

class MenuView():
    def view_menu(request):
        products = Product.objects.all()
        return render(request, 'mainmenu.html', {'products':products})

    def add_to_order(request, id):
        # Add product with id into basket
        print(id)
        return MenuView.view_menu(request)

MENU = []
current_order = []
order_price = 0

        
class MenuItem(ABC): #component
    #abstract function for get products
    @abstractmethod
    def getproduct():
        return
        
class MenuProduct(MenuItem): #leaf
    def __init__(self, name, price):
        self.name = name
        self.price = price

        #this has an implementaon of abstract func where all it does is return itself
        #burgerscategory.add(burger)
    def getproduct(self): 
        return self    

class MenuCategory(MenuItem): #composite
        #all this does is call getproduct on all its child objects
        #this has a list of menu items in it
        #get product function where it just loops through the menu items
        #then calls getproduct in menuproduct on each one
        def __init__(self):
            self.itemsList = MENU

        def getproduct(self):
            products = []
            for x in self.itemsList:
                products.append(x.getproduct())           
            return products

        def addProduct(self,item):
            self.itemsList.append(item)
