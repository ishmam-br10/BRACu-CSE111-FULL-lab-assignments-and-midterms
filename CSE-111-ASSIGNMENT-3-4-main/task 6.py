class Customer:
    def __init__(self, name):
        self.name = name
    def greet(self, nam = None):
        if nam == None:
            print("Hello!")
        else:
            print(f"Hello {nam} !")

    def purchase(self, *items):
        self.count = len(items)
        print(f"{self.name}, you purchased {self.count} item(s):")
        for i in items:
            print(f"{i}")


#Driver code
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")
