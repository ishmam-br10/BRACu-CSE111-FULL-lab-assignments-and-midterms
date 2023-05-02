class player :
    team_run = 0
    def __init__(self, run):
        self.run = run
    def hit_four(self):
        self.run = self.run + 4
        player.team_run = player.team_run +4
    def hit_six(self):
        self.run = self.run + 6
        player.team_run = player.team_run + 6

###################### COMMAND LINE

sakib = player(0)
tamim = player(0)
sakib.hit_six()
sakib.hit_six()
tamim.hit_four()
tamim.hit_six()
print(sakib.run)
print(tamim.run)
print(player.team_run)
