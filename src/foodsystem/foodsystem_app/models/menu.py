from abc import abstractmethod, ABC

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

def addToCart(MenuProduct):
    current_order.append(MenuProduct)
    return current_order

def removeFromCart(MenuProduct):
    if MenuProduct in current_order:
        current_order.remove(MenuProduct)




burger = MenuProduct("Burger",5)
coffee = MenuProduct("Coffee",3)

food = MenuCategory()
food.addProduct(burger)
print(food.getproduct())

addToCart(burger)
print(current_order)
removeFromCart(burger)
print(current_order)

