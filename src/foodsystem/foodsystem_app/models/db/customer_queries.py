from foodsystem_app.models.db.customer import Customer

class Customer_Queries():
    ''' 
    This class is built to take in all the 
    Customer class queries made in views
    '''
    def __init__(self):
        pass

    def create_account(self, id, email):
        if (self.check_if_email_exists(email)):
            print("Email already exist ! please choose another one.")
        else:
            customer = Customer()
            customer.id = id
            customer.email = email
            customer.save()
            print(customer.id + " added !")

    # For now I am under impression that customers can have only one acc with their email
    def check_if_email_exists(email):
        if(Customer.objects.filter(email = email).exists()):
            return True
        else:
            return False

    def get_all_customer_list():
        return Customer.object.all()

    def get_customer_obj(customerId):
        customer = Customer.objects.filter(id = customerId)
        return customer[0]

    def get_customer_email(customerId):
        customer = Customer.objects.filter(id = customerId)
        return customer['email']

    def get_customer_id(email):
        customer = Customer.objects.filter(email = email)
        return customer['id']

    '''
    Below are all setter functions for Customer objects
    '''

    # WIP need it to avoid duplication in database
    def set_customer_email(self, customerId, newEmail):
        if(self.check_if_email_exists(newEmail)):
            print("This email already exists, please use different email")
        else:
            Customer.objects.filter(id = customerId).update(email = newEmail)
            print("Customer with " + customerId + "ID "+ "email changed !")

