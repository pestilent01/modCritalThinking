
import ItemToPurchase

class ShoppingCart:
    
    def __init__(self,customerName="none", currentDate="January 1, 2020"):
        #setup the cartItem list
        self.cartItems = []
        self.customerName = customerName
        self.currentDate = currentDate
        self.maxWidth = 100

    def add_item(self, item:ItemToPurchase.ItemToPurchase):
        #add cart item
        self.cartItems.append(item)

    def remove_item(self, itemName):
        #remove cart item
        for item in self.cartItems:
            if item.item_name == itemName:
                self.cartItems.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item:ItemToPurchase.ItemToPurchase):
        #modify cart item
        for i in range(len(self.cartItems)):
            if item.item_name != "none" and item.item_price > 0.0 and item.item_quantity > 0 and self.cartItems[i].item_name == item.item_name:
                self.cartItems[i].item_quantity = item.item_quantity
                self.cartItems[i].item_price = item.item_price
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return len(self.cartItems)
    
    def get_cost_of_cart(self):
        total = 0
        for item in self.cartItems:
            total += item.getItemTotal()
        return total
    
    def print_total(self):
        if (len(self.cartItems) == 0):
            print("SHOPPING CART IS EMPTY".center(self.maxWidth))
            return
        header = f"{self.customerName}'s Shopping Cart - {self.currentDate}"
        self.print(header)
        subHeader = f"Number of Items: {self.get_num_items_in_cart()}"
        self.print(subHeader)
        self.printItems()
        self.printFooter(self.get_cost_of_cart())

    def print_descriptions(self):
        header = f"{self.customerName}'s Shopping Cart - {self.currentDate}"
        if (len(self.cartItems) == 0):
            print("SHOPPING CART IS EMPTY".center(self.maxWidth))
            return
        self.print(header)
        self.print("Item Descriptions")
        self.printItemDescriptions()

    def print(self, title):
        #print the TOTAL COST header, but we want it centered.
        print(title.center(self.maxWidth), "\n") #add additional new line after the title
    
    def printItems(self):
        #display the the items in the cart
        for item in self.cartItems:
            text = f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.getItemTotal():.2f}"
            self.print(text)

    def printItemDescriptions(self):
        #display the the items in the cart
        for item in self.cartItems:
            itemDescr = f"{item.item_name}: {item.item_description}"
            self.print(itemDescr)

    def printFooter(self, total):
        #print the total cost of all the items in the cart, but we wantt it centered
        total = "Total: ${:.2f}".format(total)
        print(total.center(self.maxWidth))

    def getTotalCost(self):
        #Get cart total
        total = 0
        for item in self.cartItems:
            total += item.getItemTotal()
        return total
    


    