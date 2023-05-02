class TARCsDine:
    def __init__(self, name, balance, weight):
        self.name = name
        self.balance = balance
        self.weight = weight
        self.weight2 = weight.replace('kg', '')
        self.order = {}
        self.balance2 = balance.replace('tk','')
    def details(self):
        return (f'Customer name: {self.name} \n'
                f'Customer Budget: {self.balance} \n'
                f'Customer Weight: {self.weight}')

    def addOrder(self, *orders):
        count = 0
        order_count = 0


        if len(orders) <= 2:
            for i in range(0,len(orders)-1):
                self.order[orders[i]] = orders[i+1]
                price = orders[i+1].replace('tk','')
                count = count + int(price)
                order_count = order_count+1
        else:
            for i in range(0,len(orders),2):
                self.order[orders[i]] = orders[i+1]
                price = orders[i+1].replace('tk','')
                count = count + int(price)
                order_count = order_count+1

        if int(self.weight2) > 80 and order_count > 2:
            return (f"Ordered Items: {self.order} \n"
                    "Order Unsuccessful. Sorry, Sir. Your budget seems fine but "
                    "still, we can't take all your orders. Your weight is too much." 
                    "You should reduce your order to keep fit. We give more "
                    "priority to our customers' health rather than our profit.")

        elif int(self.balance2) < count :
            return(f"Ordered Items: {self.order} \n"
                   f"Order unsuccessful blah blah blah")

        else:
            return (f"Ordered Items: {self.order} \n"
                    f"Order successful")

# Write your code here
customer1 = TARCsDine("Aminul","550tk","80kg")
customer2 = TARCsDine("Mukul","800tk","75kg")
customer3 = TARCsDine("Shafin","1600tk","112kg")
customer4 = TARCsDine("Alisha","300tk","54kg")
print("##########################"
)
print(customer1.details())
print(customer1.addOrder("Pasta Basta","350tk"))
print("##########################"
)
print(customer2.details())
print(customer2.addOrder("Oven baked chicken pasta","450tk","The Blueberry pancake", "200tk"))
print("##########################"
)
print(customer3.details())
print(customer3.addOrder("Bullet Pizza 12inch","1000tk","Chicken Chowmien", "260tk","Ara Ara Beef Ramen", "299tk"))
print("##########################"
)
print(customer4.details())
print(customer4.addOrder("Cheese Cake","200tk","Kitkat Shake", "150tk"))