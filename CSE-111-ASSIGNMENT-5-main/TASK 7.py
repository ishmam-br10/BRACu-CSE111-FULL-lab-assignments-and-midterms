class Dolls:
    def __init__(self, name, price, check = False):
        self.__name = name
        self.__price  = price
        ## ADDED LINE
        self.check = check
        #================

    def __gt__(self, other):
        return self.__price > other.__price

    def __add__(self, other):
        return Dolls(self.__name+' '+ other.__name,self.__price + other.__price, True)

    def detail(self):
        ## ADDED CONDITION
        if self.check == False:
            return(f'Doll: {self.__name}\nTotal Price: {self.__price} taka')
        else:
            return (f'Dolls: {self.__name}\nTotal Price: {self.__price} taka')
## DRIVER CODE
obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
print(obj_5.added)
print(obj_5.__dict__)
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
