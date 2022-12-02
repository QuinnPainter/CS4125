import six
from abc import ABCMeta
from decimal import Decimal

@six.add_metaclass(ABCMeta)
class Abstract_Price(object):

   def get_price(self):
      pass

class Concrete_Price(Abstract_Price):
   def __init__(self, price):
      self.price = price
      
   def get_price(self):
      return self.price

@six.add_metaclass(ABCMeta)
class Abstract_Price_Decorator(Abstract_Price):
   
   def __init__(self,decorated_price):
      self.decorated_price = decorated_price
   
   def get_price(self):
      return self.decorated_price.get_price()
      
class FlatDiscount(Abstract_Price_Decorator):
   
   def __init__(self,decorated_price, discount_value):
      Abstract_Price_Decorator.__init__(self,decorated_price)
      self.discount_value = discount_value
   
   def get_price(self):
      return self.decorated_price.get_price() - self.discount_value

class PercentageDiscount(Abstract_Price_Decorator):
   def __init__(self,decorated_price, discount_value):
      Abstract_Price_Decorator.__init__(self,decorated_price)
      self.discount_value = discount_value

   def percentageToNumber(self):
       return ((self.decorated_price.get_price() * self.discount_value) / 100)
   
   def get_price(self):
      return self.decorated_price.get_price() - self.percentageToNumber()

# Factory method + decorator pattern
def createDiscount(price_before_discount, discount_coupons):
    decorated_price = Concrete_Price(price_before_discount)
    # making sure all coupons are in lower case for conditions
    for coupon in discount_coupons:
        coupon = coupon.lower()

    # Decorator in action
    for coupon in discount_coupons:
        discountType = coupon[0:2]
        discountValue = coupon[2:4]
        if(discountType == "fd"):
            decorated_price = FlatDiscount(decorated_price, Decimal(discountValue))
        elif(discountType == "pd"):
            decorated_price = PercentageDiscount(decorated_price, Decimal(discountValue))
	
    return decorated_price
	    
'''
code below was to see it working
discount_coupons = ["fd02", "fd04", "pd10"]
obj = createDiscount(10, discount_coupons)
print('Cost: '+str(obj.get_price()))
output was "Cost: 3.6" which is right
because 10 - 2 - 4 = 4 then 10 percent of 4 is 0.4 so 4 -0.4 = 3.6
'''