import requests
from player import Player

def PlayerReader(url):
    response = requests.get(url).json()
    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    
    return players