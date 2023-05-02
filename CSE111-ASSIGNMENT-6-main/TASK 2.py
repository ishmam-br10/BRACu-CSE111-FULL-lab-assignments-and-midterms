class Assassin:
    assasin = 0
    rate = 100
    def __init__(self, name, rate):
        Assassin.assasin += 1
        self.name = name
        self.rate = rate

    @classmethod
    def failureRate(cls, name, failure):
        new = Assassin(name, (cls.rate- failure))
        return new

    @classmethod
    def failurePercentage(cls, name, percent):
        new1 = Assassin(name, (cls.rate - int(percent.replace('%',''))))
        return new1

    def printDetails(self):
        print(f'Name: {self.name}\nSuccess rate: {self.rate}%\nTotal number of Assassin:{Assassin.assasin}')


# Write your code here

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
