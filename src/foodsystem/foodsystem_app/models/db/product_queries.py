from foodsystem_app.models.db.product import Product
from foodsystem_app.models.db.product_category import ProductCategory

class ProductQueries():
    ''' 
    This class is built to take in all the 
    Product class queries made in views
    '''
    def __init__(self):
        pass

    def create_product(name, price, image, categoryName):
        product = Product()
        product.name = name
        product.price = price
        product.image = image
        product.category = ProductQueries.get_category_by_name(categoryName)
        product.save()
        print(product.name + " added !")

    def create_category(name):
        cat = ProductCategory()
        cat.name = name
        cat.save()

    def get_all_products_list():
        return Product.objects.all()

    def get_all_categories():
        return ProductCategory.objects.all()

    def get_category_by_name(name):
        return ProductCategory.objects.filter(name = name)[0]

    def get_product_by_id(id):
        product = Product.objects.filter(id = id)
        return product[0]

    def get_product(self, prodName):
        product = Product.objects.filter(name = prodName)
        return product[0]

    def get_product_price(prodName):
        product = Product.objects.filter(name = prodName)
        return product[0].price()
