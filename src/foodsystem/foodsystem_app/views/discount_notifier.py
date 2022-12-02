from abc import abstractmethod, ABC

class NotifierContext():
    def setStrategy(self, newStrategy):
        self.strategy = newStrategy
    
    def sendNotification(self, message):
        self.strategy.sendNotification(message)

class NotifierStrategy(ABC):
    @abstractmethod
    def sendNotification(message):
        pass

class EmailConcreteStrategy(NotifierStrategy):
    def sendNotification(message):
        # Email the message to the customer
        # (since we have no code to actually send an email, printing it will do)
        print(message)
        
class SMSConcreteStrategy(NotifierStrategy):
    def sendNotification(message):
        # SMS the message to the customer
        # (since we have no code to actually send an SMS, printing it will do)
        print(message)
