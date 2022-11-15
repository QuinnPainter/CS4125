from abc import ABC, abstractmethod

class DiscountNotifier(ABC):
    # should pass in a Discount and Customer here
    @abstractmethod
    def update():
        pass

class DiscountNotifierSMS(DiscountNotifier):
    def update():
        # Send an SMS message to the customer
        pass

class DiscountNotifierEmail(DiscountNotifier):
    def update():
        # Send an email to the customer
        pass
