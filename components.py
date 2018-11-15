# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)
        
    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print("6969696969696969696969696969696969696969696\n")
        for product in self.products:
            print(product)
        print("\n")
        print("6969696969696969696969696969696969696969696\n")


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return ("Product Name: " + self.name + " \n" + "Description: " + self.description + ". \n" + "Price: " + str(self.price) + "\n")
      
        

class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []


    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)


    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0 
        for product in self.products:
            total = total + product.price
        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("6969696969696969696969696969696969696969696\n")
        print("This is your receipt: \n")
        for product in self.products:
            print(product)

        print("The total price is: "+str(self.get_total_price()) + "KD.\n")
        print("6969696969696969696969696969696969696969696\n")

        

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!

        self.print_receipt()
        confirmation = input("Confirm your order please by typing \"yes\" to confirm or \"no\" to cancel: \n")
        if confirmation.lower() == "yes":
            print("\nYour order has been placed.")
            print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
        elif confirmation.lower() == "no":
            print("\nYour order has been cancelled.")
            print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")


