class Anime_Toys:
    def __init__(self, name, anime, taka, appear, size, auto = 'not automated'):
        list1 = appear.split(' - ')
        self.name = name
        self.anime = anime
        self.taka = taka.replace('TK', '')
        self.size = size
        self.auto = auto
        apperance = ''
        for i in list1:
            apperance = apperance + i.join(', ')
        self.apperance = apperance[1:]


class Shopping_Cart:
    def __init__(self, name, budget = 20000):
        self.custname = name
        self.budget = budget

        self.bought = []
        self.total_cost = 0
        self.total = 0
    def buy_toys(self, *toys):
        self.toys = toys
        for i in toys:
            self.total = int(i.taka) + self.total
            if self.total > self.budget:
                print(f"{self.custname}, you can't buy anymore toys since it crosses your budget")
                break
            else:
                print('Toy purchased')
                self.bought.append(i)
                self.total_cost = int(i.taka) + self.total_cost
    def print_shopping_details(self):
        print(f'Coustomer: {self.custname}')
        print(f'Budget: {self.budget}')
        for i in range (len(self.bought)):
            print(f'-------{i+1}-------')
            print(f'Toy: {self.bought[i].name}, Anime: {self.bought[i].anime}')
            print(f'Appearance: {self.bought[i].apperance}')
            print(f'Size: {self.bought[i].size}')
            print(f'The toy is {self.bought[i].auto}')



### DRIVER

a1 = Anime_Toys("Pikachu","Pokemon","2000TK","yellow","small","automated")
a2 = Anime_Toys("Naruto","Naruto","2800TK","yellow hair - orange clothes - blue sandals","medium")
a3 = Anime_Toys("Pikachu","Pokemon","4000TK","yellow","large","automated")
a4 = Anime_Toys("Mikasa","Attack onTitans","3500 TK","white shirt - black pants - red scarf","small","not automated")
c1 = Shopping_Cart("Steven Brown")
c1.buy_toys(a1,a2)
print("=================================")
c1.print_shopping_details()
print("=================================")
c1.buy_toys(a3)
c1.buy_toys(a4)
print("=================================")
c1.print_shopping_details()
print("=================================")
print(f"TOTAL COST = {c1.total_cost} TK")
print("=================================")
c2 = Shopping_Cart("Riley Renolds", 8000)
print("=================================")
c2.buy_toys(a3,a4,a2)
print("=================================")
c2.print_shopping_details()
print("=================================")
print(f"TOTAL COST = {c2.total_cost} TK")
print("=================================")
c2.buy_toys(a1,a2)