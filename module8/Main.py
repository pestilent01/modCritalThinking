from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart
from datetime import datetime

def print_menu():
    print("a","-", "Add item to cart")
    print("r","-", "Remove item from cart")
    print("c","-", "Change item quantity")
    print("i","-", "Output items' descriptions")
    print("o","-", "Output shopping cart")
    print("q","-", "Quit")
    print("Choose an option:")

def print_cart(cart:ShoppingCart):
    print("OUTPUT SHOPPING CART")
    print()
    cart.print_total()

def print_descriptions(cart:ShoppingCart):
    print("OUTPUT ITEMS' DESCRIPTIONS")
    print()
    cart.print_descriptions()

def getUserInput(prompt=""):
    print(prompt)    # custom prompt
    item = ItemToPurchase() # create an instance of the item class

    print("Enter the item name:\n")
    itemName = input() 
    print("Enter the item description:\n")
    itemDescription = input()
    print("Enter the item price:\n")
    itemPrice = float(input())
    print("Enter the item quantity:\n")
    itemQty = int(input())
    #set the values to the item object
    item.item_name = itemName
    item.item_price = itemPrice
    item.item_description = itemDescription
    item.item_quantity = itemQty

    return item

if __name__ == "__main__":
    
    #get the customer name and date
    customerName = input("Enter customer's name:\n")
    currentDate = input("Enter today's date:\n") 
    print()
    print("Customer name:", customerName)
    print("Today's date:", currentDate)
    print()

    cart = ShoppingCart(customerName, currentDate)

    selection = ""
    while selection != "q":
        print_menu()
        selection = input()
        if selection == "a":
            print("ADD ITEM TO CART")
            item = getUserInput()
            cart.add_item(item)
        elif selection == "r":
            print("REMOVE ITEM FROM CART")
            itemName = input("Enter name of item to remove:\n")
            cart.remove_item(itemName)
        elif selection == "c":
            print("CHANGE ITEM QUANTITY")
            itemName = input("Enter the item name:\n")
            items = [item for item in cart.cartItems if item.item_name == itemName]
            if len(items) == 0:
                print("Item not found.\n")
                continue
            else:
                item = items[0]
                item.item_quantity = int(input("What is the new quantity\n"))
            cart.modify_item(item)
        elif selection == "i":
            print_descriptions(cart)
        elif selection == "o":
            print_cart(cart)
        elif selection == "q":
            print("Exit")
        else:
            print("Please select from the menu")
        
        print() # add some space
