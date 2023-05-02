class Wadiya():
    def __init__(self):
     self.name = 'Aladeen'
     self.designation = 'President Prime Minister Admiral General'
     self.num_of_wife = 100
     self.dictator = True

# DRIVER CODE
print("Part 1:")
p1 = Wadiya()
print(f"Name of President: {p1.name}")
print(f"Designation: {p1.designation}")
print(f"Number of wife: {p1.num_of_wife}")
print(f"Is he/she dictator: {p1.dictator}")

print("Part 2:")
p2 = Wadiya()
p2.name = "Donald Trump"
p2.designation = "President"
p2.num_of_wife = 1
p2.dictator = False
print(f"Name of President: {p2.name}")
print(f"Designation: {p2.designation}")
print(f"Number of wife: {p2.num_of_wife}")
print(f"Is he/she dictator: {p2.dictator}")