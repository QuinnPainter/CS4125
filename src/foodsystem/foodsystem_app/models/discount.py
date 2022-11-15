class Price():
    """
    Interface for getting a price
    """

    def get_price(self):
        pass

class BasicPrice(Price):
    """
    Implements interface Price
    This is a basic price with no discount applied
    """

    _price = 10.00

    def get_price(self):
        return self._price


class DiscountedPrice(Price):
    """
    Implements interface Price
    This is the base class for discounted prices.
    It has a variable 'basic_price',
    which is the basic price that is passed in which
    is going to be discounted by the get_price method
    e.g.
                  (* 0.5)           (* 0.8)
            4.0      <-    8.00        <-   10.00
    BirthdayDiscount(ManicMondayDiscount(my_basic_price))
    """

    def __init__(self, basic_price):
        self.basic_price = basic_price

    def get_price(self):
        return self.basic_price.get_price()

class ManicMondayDiscount(DiscountedPrice):
    """
    This class inherits DiscountedPrice
    It has its own variable _discount which it applies to
    basic_price when get_price is called
    """

    _discount = 0.8

    def __init__(self, basic_price):
        super().__init__(basic_price)

    def get_price(self):
        return (self.basic_price.get_price() * self._discount)

class BirthdayDiscount(DiscountedPrice):
    """
    This is another class that inherits DiscountedPrice
    """

    _discount = 0.5

    def __init__(self, basic_price):
        super().__init__(basic_price)

    def get_price(self):
        return (self.basic_price.get_price() * self._discount)

def no_discount():
    """
    Calling get_price on a BasicPrice simply returns _price
    """
    my_price = BasicPrice()
    print("Price with no discount applied")
    print(my_price.get_price())

def manic_monday():
    """
    Calling get_price on a DiscountedPrice first gets its own basic_price
    (which could be a BasicPrice with a _price equal to 10.00
    or it could be another DiscountedPrice with its own basic_price)
    then it multiplies the _discount variable and returns the discounted price
    """
    my_price = BasicPrice()
    my_price = ManicMondayDiscount(my_price)
    print("Price on Manic Monday")
    print(my_price.get_price())

def both():
    my_price = BasicPrice()
    my_price = BirthdayDiscount(ManicMondayDiscount(my_price))
    print("Price on Manic Monday and it's your Birthday")
    print(my_price.get_price())

if __name__ == '__main__':
    no_discount()
    manic_monday()
    both()
