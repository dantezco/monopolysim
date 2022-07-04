"""
This module contains players and player logic
"""
import random

from src.constants import (
    LABEL_CAUTIOUS,
    LABEL_DEMANDING,
    LABEL_IMPULSIVE,
    LABEL_UNPREDICTABLE,
    STARTING_MONEY,
)


class Player:
    """Contains player data and its control methods"""

    def __init__(self, archetype: str, money: int) -> None:
        self.archetype: str = archetype
        self.position: int = 0
        self.money: int = money

    def spend(self, value: int):
        """Spend value amount of money from the player"""
        self.money -= value

    def earn(self, value: int):
        """Player earns value amount of money"""
        self.money += value

    def still_in_game(self):
        """Players with debts are out of the game"""
        return self.money > 0


def init_players():
    """Initializes an array with all the players in a random order for playing"""
    players: list = [
        Player(LABEL_DEMANDING, STARTING_MONEY),
        Player(LABEL_CAUTIOUS, STARTING_MONEY),
        Player(LABEL_IMPULSIVE, STARTING_MONEY),
        Player(LABEL_UNPREDICTABLE, STARTING_MONEY),
    ]
    random.shuffle(players)
    return players
