from abc import abstractmethod
from foodsystem_app.models.db.product_queries import ProductQueries

'''
Code below shows both Factory and Decorator patterns combined
'''

class Food():
    @abstractmethod
    def get_price():
        pass
    @abstractmethod
    def get_name():
        pass

class ConcreteFood(Food):
    def __init__(self, food_name):
        self.name = food_name
        self.price = ProductQueries.get_product_price(food_name)
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name

class AbstractFoodDecorator(Food):
    def __init__(self,decorated_food, food_name):
        self.decorated_food = decorated_food
        self.name = food_name
   
    def get_price(self):
        return self.decorated_food.get_price()
    
    def get_name(self):
        return self.name


class EatableFoodSmall(AbstractFoodDecorator):
    def __init__(self,decorated_food):
        AbstractFoodDecorator.__init__(self,decorated_food)
   
    def get_price(self):
        percentage = 20
        reduce_price = (self.decorated_food.get_price() * percentage) / 100
        return self.decorated_food.get_price() + reduce_price

class EatableFoodLarge(AbstractFoodDecorator):
    def __init__(self,decorated_food):
        AbstractFoodDecorator.__init__(self,decorated_food)
   
    def get_price(self):
        percentage = 20
        extra_price = (self.decorated_food.get_price() * percentage) / 100
        return self.decorated_food.get_price() + extra_price
    
    def get_name(self):
        return self.decorated_food.get_name() + 'Large'

class DrinkableFoodSmall(AbstractFoodDecorator):
    def __init__(self,decorated_food):
        AbstractFoodDecorator.__init__(self,decorated_food)
   
    def get_price(self):
        percentage = 10
        reduce_price = (self.decorated_food.get_price() * percentage) / 100
        return self.decorated_food.get_price() + reduce_price
    
    def get_name(self):
        return self.decorated_food.get_name() + 'Large'

class DrinkableFoodLarge(AbstractFoodDecorator):
    def __init__(self,decorated_food):
        AbstractFoodDecorator.__init__(self,decorated_food)
   
    def get_price(self):
        percentage = 10
        extra_price = (self.decorated_food.get_price() * percentage) / 100
        return self.decorated_food.get_price() + extra_price
    
    def get_name(self):
        return self.decorated_food.get_name() + 'Large'

def FactoryFood(foodType, foodName):

    """Factory Method"""
    food = {
        "anyregular" : ConcreteFood,
        "eatSmall": EatableFoodSmall,
        "eatlarge": EatableFoodLarge,
        "drinkSmall": DrinkableFoodSmall,
        "drinklarge": DrinkableFoodLarge,
    }
 
    return food[foodType](foodName)

# Calls factory method after choosing the right object
def createFoodObject(foodCategory, size, name):
    food = ""
    foodCategory = foodCategory.lower()
    size = size.lower()
    # conditions for small sized foods
    if(size == "regular"):
        food = "anyregular"
    elif(size == "small"):
        if(foodCategory == "eatable"):
            food = "eat"
        elif(foodCategory == "drinkable"):
            food = "drink"
    # condition for large sized foods
    elif(size == "large"):
        if(foodCategory == "eatable"):
            food = "eatlarge"
        elif(foodCategory == "drinkable"):
            food = "drinklarge"

    # Calling factory method and return obj
    return FactoryFood(food, name)
