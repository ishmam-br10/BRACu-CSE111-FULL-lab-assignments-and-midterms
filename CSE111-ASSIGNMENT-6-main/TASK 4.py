#TASK 4
class Travel:
    time = '1:00'
    count = 0
    def __init__(self, source, destination):
        Travel.count += 1
        self.time = Travel.time
        self.source =source
        self.dest = destination

    def set_time(self, time):
        self.time = str(f'{time}:00')

    def set_source(self, sour):
        self.source =sour

    def set_destination(self, des):
        self.dest = des

    def display_travel_info(self):
        return (f"Source: {self.source}\nDestination: {self.dest}\nFlight Time: {self.time}")

# DRIVER CODE
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)