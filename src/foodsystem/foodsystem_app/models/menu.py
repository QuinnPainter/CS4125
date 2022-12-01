from abc import abstractmethod, ABC
from foodsystem_app.models.db.product_queries import ProductQueries
        
class MenuComponent(ABC):
    @abstractmethod
    def getProducts():
        return

    @abstractmethod
    def findComponentByName():
        return

# represents a product eg. burger
class MenuLeaf(MenuComponent):
    def __init__(self, id, name, price, image):
        self.id = id
        self.name = name
        self.price = price
        self.image = image

    def getProducts(self):
        return [self]

    def findComponentByName(self, name):
        if self.name == name:
            return self
        else:
            return None

# represents a category eg. drinks
class MenuComposite(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.itemsList = []

    def getProducts(self):
        products = []
        for x in self.itemsList:
            products += x.getProducts()
        return products

    def addProduct(self, item):
        self.itemsList.append(item)

    def getName(self):
        return self.name

    def findComponentByName(self, name):
        if name == self.name:
            return self
        for p in self.itemsList:
            if p.findComponentByName(name) is not None:
                return p

class Menu():
    def getMenu():
        rootComposite = MenuComposite("Menu")

        categories = ProductQueries.get_all_categories()
        for c in categories:
            newCat = MenuComposite(c.name)
            rootComposite.addProduct(newCat)

        products = ProductQueries.get_all_products_list()
        for p in products:
            newProduct = MenuLeaf(p.id, p.name, p.price, p.image)
            cat = rootComposite.findComponentByName(p.category.name)
            cat.addProduct(newProduct)
        return rootComposite
