class Team:

    def __init__(self, name):
        self.name = "default"
        self.total_player = 5
    def info(self):
        print("We love sports")
# Write your code here.

class Team_test:
    def check(self, tm):
        print("=========================")
        print("Total Player: ", tm.total_player)
        tm.info()
class FootBallTeam(Team):
    def __init__(self, team):
        self.name = team
        self.total_player = 11
    def info(self):
        print(f"Our name is = {self.name}\nWe play Football")
        super().info()
class CricketTeam(Team):
    def __init__(self, team):
        self.name = team
        self.total_player = 11
    def info(self):
        print(f"Our name is = {self.name}\nWe play Cricket")
        super().info()
f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)
