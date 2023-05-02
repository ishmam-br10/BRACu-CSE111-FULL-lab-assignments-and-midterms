class Flower:
    def __int__(self, name, color, petal):
        self.name = name
        self.color = color
        self.num_of_petal = petal
flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print('=====================')
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)
# subtask
print(f"Adress of flower1 {flower1}")
print(f"Adress of flower2 {flower2}")
if flower1 == flower2 :
    print('They are same')
else:
    print("They are different")