class DiscountNotificationSender():
    def __init__(self):
        self.subscribers = []

    def register(self, notifier):
        self.subscribers.append(notifier)
    
    def unregister(self, notifier):
        self.subscribers.remove(notifier)

    def sendNotification(self):
        for sub in self.subscribers:
            sub.update()
