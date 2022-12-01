# Singleton pattern
class Basket():
    _instance = None
    productList = []

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def addProduct(self, prod):
        self.productList.append(prod)

    def removeProduct(self, prod):
        self.productList.remove(prod)

    def getProducts(self):
        return self.productList
