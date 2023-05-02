# TASK 6
class Laptop:
    laptopCount = 0
    def __init__(self, laptopname, number):
        self.name = laptopname
        self.count = number
        Laptop.laptopCount += number

    @classmethod
    def advantage(cls):
        print("Laptops are portable")
    @classmethod
    def resetCount(cls):
        cls.laptopCount = 0

# DRIVER CODE
lenovo = Laptop("Lenovo", 5)
dell = Laptop("Dell", 7)
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)
