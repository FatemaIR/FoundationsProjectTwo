# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.OnFire.com \n"  # Give your site a name

def welcome():
    print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once! \n" % site_name)
    print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    
    for store in stores:
        print(" - " + store.name + "\n")
    

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
    else: 
        return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    while (True):
        print_stores()

        user_input = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n\n")
        if (user_input.lower() == "checkout"):
            return "checkout"

        picked_store = get_store(user_input)
        if picked_store:
            break    
        else: 
            print("\nNo store with that name. Please try again.\n")
            
    return picked_store



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

    user_pick_item = input("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above. \n Type \"back\" to go back to the main menu where you can checkout.\n")
    
    while (user_pick_item.lower() != "back"):
        for product in picked_store.products:
            if user_pick_item.lower() == product.name.lower():
                cart.add_to_cart(product)
        user_pick_item = input()
        
    return user_pick_item
    #else: 
      #  pick_store()



def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    user_pick_item = ""

    while user_pick_item.lower() != "checkout":
        user_pick_item = ""
        picked_store = pick_store()
        if picked_store == "checkout":
            break
        print("Here are all the products in this store: \n")
        picked_store.print_products()
        user_pick_item = pick_products(cart, picked_store)
    cart.checkout()
    


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
    print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
