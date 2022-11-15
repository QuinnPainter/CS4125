from foodsystem_app.models.product import Product

class Product_Queries():
    ''' 
    This class is built to take in all the 
    Product class queries made in views
    '''
    def __init__(self):
        pass

    def create_product(name, price):
        print("I was here")
        product = Product(name, price)
        product.save()
        print(product.name + ' ' +  "added !")

    def get_all_products_list():
        return Product.object.all()

    def get_product(self, prodName):
        products = self.get_all_products_list()
        for p in products:
            print(p.name)
        product = Product.objects.filter(name = prodName)
        return product[0]


    def get_product_price(prodName):
        product = Product.objects.filter(name = prodName)
        return product[0].price()