#task 5
class UberEats:
    def __init__(self, name, number, location):
        self.name = name
        self.number = number
        self.location = location
        print(f"{self.name}, welcome tp UberEats!")

    def add_items(self, *order):
        self.dic ={}
        for i in range(0,2):
            self.dic[order[i]] = order[i + 2]
        self.total = order[2] + order[3]
    def print_order_detail(self):
        return (f"User details: Name: {self.name}, Phone: \n{self.number},Address: {self.location}\nOrders: {self.dic}\nTotal Paid Amount: {self.total} ")



# DRIVER CODE

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())
