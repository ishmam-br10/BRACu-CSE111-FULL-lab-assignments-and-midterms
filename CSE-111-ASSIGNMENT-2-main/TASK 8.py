# TASK 8
class box():
    def __init__(self, list_of_dim):
        print("Creating a Box!")
        self.height = list_of_dim[0]
        self.width = list_of_dim[1]
        self.breadth = list_of_dim[2]
        print(f"Volume of the box is {list_of_dim[0] * list_of_dim[1] * list_of_dim[2]} cubic units.")

#DRIVER CODE

print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
