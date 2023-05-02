# TASK 9
class Batsman:
    def __init__(self,*info):
        if len(info) == 2:
            self.name = 'New Batsman'
            self.run = info[0]
            self.balls = info[1]
        else:
            self.name = info[0]
            self.run = info[1]
            self.balls = info[2]



    def setName(self, nam):
        self.name = nam

    def printCareerStatistics(self):
        print(f"Name: {self.name} \nRuns Scored: {self.run} ,Balls Faced: {self.balls}")

    def battingStrikeRate(self):
        return (f"{(self.run / self.balls)*100}")

# DRIVER CODE
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
