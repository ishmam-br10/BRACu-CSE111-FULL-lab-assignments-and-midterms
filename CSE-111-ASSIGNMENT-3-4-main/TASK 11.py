class TaxiLagbe:
    def __init__(self, number, loc):
        self.number = number
        self.area = loc
        self.passenger_list = {}
    def addPassenger(self, *passengers):

        self.count = 0
        for key in self.passenger_list.keys():
            self.count = self.count + 1
        #print(self.passenger_list)
        if self.count < 4:
            for i in passengers:
                list1 = []
                list1 = i.split("_")
                self.passenger_list[list1[0]] = int(list1[1])
                print(f"Dear {list1[0]}! Welcome to TaxiLagbe")
            for keys in self.passenger_list.keys():
                pass
        else:
            print('Taxi Full! No more passengers can be added.')
    def printDetails(self):
        print(f'Trip info for Taxi number:{self.number}')
        print(f"This taxi can cover only {self.area} area.")
        self.counter = 0
        for i in self.passenger_list.keys():
            self.counter = self.counter + 1
        print(f"Total passengers: {self.counter}")
        self.fare = 0
        self.list0 = []
        for key, value in self.passenger_list.items():
            self.fare = (self.fare) + int(value)
            self.list0.append(key)
        me = 0
        print("Passengers list: ")
        for i in self.list0:
            me = me + 1
            if me != len(self.list0):
                print(i, end=', ')
            else:
                print(i, end= '')
        print('')
        print(f"Total collected fare: {self.fare} taka")

# DRIVER CODE
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
