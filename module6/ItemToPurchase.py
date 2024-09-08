class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0.00, description="none", item_quantity=0):
        #initialize the item name, price and quantity
        self.item_name = item_name
        self.item_price = item_price
        self.item_description = description
        self.item_quantity = item_quantity

    def getItemTotal(self):
        #calculate the total cost of the item
        return self.item_price * self.item_quantity

