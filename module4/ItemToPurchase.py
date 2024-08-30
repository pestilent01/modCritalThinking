class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0.00, item_quantity=0):
        #initialize the item name, price and quantity
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def getItemTotal(self):
        #calculate the total cost of the item
        return self.item_price * self.item_quantity
    
    def getItemDescription(self):
        #return a string that describes the item and it's line item cost
        itemDescription = "{0} {1} @ ${2:.2f} = ${3:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.getItemTotal())
        return itemDescription
    
    def print_item_cost(self):
        #print the line item cost to screen
        itemDescription = self.getItemDescription()
        print(itemDescription)


class CheckOut:
    
    def __init__(self):
        #setup the cartItem list
        self.cartItems = []

    def addItem(self, item):
        #add an item to the cart
        self.cartItems.append(item)

    def printHeader(self, title, width=50):
        #print the TOTAL COST header, but we want it centered.
        print(title.center(width), "\n") #add additional new line after the title
        
    
    def printItems(self):
        #display the the items in the cart
        for item in self.cartItems:
            item.print_item_cost()

    def printFooter(self, total, width=50):
        #print the total cost of all the items in the cart, but we wantt it centered
        total = "\nTotal: ${:.2f}".format(total)
        print(total.center(width))

    def getMaxWidth(self):
        #calculate the maximum width of the item description for all items in the cart.
        max_width = 0
        for item in self.cartItems:
            description = item.getItemDescription()
            if len(description) > max_width:
                max_width = len(description)
        return max_width
    
    def getTotalCost(self):
        #calculate the total cost of all the items in the cart
        
        total = 0
        for item in self.cartItems:
            total += item.getItemTotal()
        return total
    
    def printReceipt(self):
        #print the receipt to the screen.
        maxWidth = self.getMaxWidth()
        title = "TOTAL COST"
        self.printHeader(title, maxWidth) #print the receipt header
        self.printItems() #print out each items in the cart with its total
        self.printFooter(self.getTotalCost(), maxWidth) #print the total cost at the end

        
def getUserInput(prompt=""):
    print(prompt)    # custom prompt
    item = ItemToPurchase() # create an instance of the item class

    print("Enter the item name:")
    itemName = input() 
    print("Enter the item price:")
    itemPrice = float(input())
    print("Enter the item quantity:")
    itemQty = int(input())
    #set the values to the item object
    item.item_name = itemName
    item.item_price = itemPrice
    item.item_quantity = itemQty

    return item

if __name__ == "__main__":

    item1 = getUserInput("Item 1") #read the user input for the first item
    item2 = getUserInput("Item 2") #read the user input again for the second item
    checkout = CheckOut() # create an instance of a shopping cart that will do our calculations for us
    checkout.addItem(item1) #add the items to the shopping cart
    checkout.addItem(item2) #add the items to the shopping cart
    checkout.printReceipt() #print the receipt of the whole shopping cart