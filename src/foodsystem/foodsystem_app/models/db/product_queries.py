from foodsystem_app.models.db.product import Product

class Product_Queries():
    ''' 
    This class is built to take in all the 
    Product class queries made in views
    '''
    def __init__(self):
        pass

    def create_product(name, price):
        print("I was here")
        product = Product()
        product.name = name
        product.price = price
        product.save()
        print(product.name + " added !")

    def get_all_products_list():
        return Product.object.all()

    def get_product_by_id(id):
        product = Product.objects.filter(id = id)
        return product[0]

    def get_product(self, prodName):
        product = Product.objects.filter(name = prodName)
        return product[0]


    def get_product_price(prodName):
        product = Product.objects.filter(name = prodName)
        return product[0].price()