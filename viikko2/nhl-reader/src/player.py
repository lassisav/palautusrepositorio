class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
        self.nationality = dict['nationality']
    
    def __str__(self):
        return f"{self.name:20}" +  self.team + "   " + str(self.goals) + " + " + str(self.assists) + " = " + str(self.points)
    
    def getNat(self):
        return self.nationality
