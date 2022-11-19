#Checkout functionality
#Complete order
#Show basket
#Show total price

import time

def paymentSys():

    print("""
    How do you want to pay?
    -----------------------
    1: Cash
    2: Card
    """)

    cashOrCard = int(input("Enter: "))

    if cashOrCard == 1:
        print("Please proceed to till :)")

    elif cashOrCard == 2:
        print("Enter card number: ")
        cardNo = int(input("Card number: "))
        #if len(cardNo) != 16:
            #print("Incorrect number of digits...")
            #paymentSys()

        print("Enter expiry...")
        int(input("Expiry: "))

        print("Enter CVV: ")
        int(input("CVV: "))

        print("processing...")
        time.sleep(3)

        print("All good! Please go to collect your food :)")
        exit()
    
    else:
        print("Invalid command!")
        paymentSys()        

    return "Thank You!"


print("""
Your basket
-------------
Press one of the following:
1: Remove an item 
2: View basket
3: Proceed to payment
0: Go back
""")

decision = int(input("Enter: "))

while decision!= 0:
    if decision == 1:
        item = int(input("Which item do you want to remove?: "))
        #del(whatever menu is called[item])

    elif decision == 2:
        #for item in menu
        #print(item, ":", menu)
        print("OK")

    elif decision == 3:
        paymentSys()

else:
    print("Closing checkout...")

#2 different files
#One for viewing and editing your basket
#One for entering card or paying cash

class order(shop):

    # Define function to add product into the cart
    #def add_to_cart(self, item):
        # Add product into the cart
        #self.cart_items.append(item)
        #print("%s is added in the cart." %(item))

    def view_cart():
        print("""
        Your basket
        ------------
        """)
        print("Burger", "$7")
        print("Chips", "$")
        print("Fanta", "$3")
        print("""
        Total
        ------
        """)
        #cart_total()



    # Define function to remove product from the cart
    def remove_from_cart(self, obj):
        #THIS WILL BE WHEN CLICK  REMOVE BUTTON CALL THIS
        item = input("Enter the product name:")
        if item in obj.cart_items:
            # Remove product from the cart
            obj.cart_items.remove(item)
            print("Product is removed from the cart")
            # Open the file to search the price of the product
            #with open('products.txt') as f:
                #for line in f:
                    #fieldList = list(line.split(","))
                    #for val in fieldList:
                        #if item == val.strip():
                            # Remove the price of the removed product from the cart amount
                            #obj.cart_amount = obj.cart_amount - int(fieldList[2].strip())  
        else:
            print("Product does not exist in the cart.")
       
    # Define function to display the cart items
    def display_cart(self, obj):
        # Check the cart amount to find out the cart is empty or not
        if obj.cart_amount > 0:
            # Display the added cart items
            print("\nYou have added the following item(s) in your cart:\n")
            for val in self.cart_items:
                print(val)
           
            # Print the total cart amount
            print("\n%s%s%d%s"  %(fg(25), 'Total amount:$', obj.cart_amount, attr(0)))

            # Display the second menu
            print("\n1. Add Product")
            print("2. Remove Product")
            print("3. Confirm Payment")
            print("4. Cancel")
            ans = input("\nType 1 or 2 or 3 or 4:")
            return ans

        else:
            # Print message if the cart is empty
            print("You cart is empty.")
            return 0
    