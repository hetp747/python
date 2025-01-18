class Shopping:

    def __init__(self):
        self.items = []

    def add_item(self, itemname, qty, cate):
        item = (itemname, qty, cate)
        self.items.append(item)

    def remove_item(self, itemname):
        for item in self.items:
            if item[0] == itemname:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

cart = Shopping()
cart.add_item("Papaya", 100 , "fruits")
cart.add_item("Guava", 200, "fruits")
cart.add_item("Orange", 150, "fruits")
cart.add_item("banana",300, "fruits")
# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
cart.remove_item("banana")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])
total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)
