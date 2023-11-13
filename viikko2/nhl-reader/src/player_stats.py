from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        """Funktio tulostaa annetun kansallisuuden pelaajat pistejärjestyksessä."""
        players = []
        for player in self.reader:
            if player.getNat() == nat:
                players.append(player)

        players = sorted(players, key = lambda x: x.points, reverse=True)
    
        print("Players from "  + nat + ":\n")
        for player in players:
            print(player) 