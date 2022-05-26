import char1
import char2
from player import Player


class PlayerService:
    def __init__(self):
        self.players: list[Player] = self.get_players()

    def get_players(self) -> list[Player]:
        return [Player(char1.skills, char1. health), Player(char2.skills, char2.health)]

    def get_display_list(self) -> dict[int, Player]:
        display_list: dict[int, Player] = {}
        for i in range(len(self.players)):
            display_list[i] = self.players[i]
        return display_list
