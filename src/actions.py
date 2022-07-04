"""
This module contains logic for the buying action
"""

import random

from src.board import House
from src.constants import (
    CAUTIOUS_MIN_RENT,
    DEMANDING_MIN_LEFTOVER,
    LABEL_CAUTIOUS,
    LABEL_DEMANDING,
    LABEL_IMPULSIVE,
    LABEL_UNPREDICTABLE,
)
from src.players import Player


class Buy:
    """Logic for action of buying the current house.
    Encapsulates the multiple possible behaviours of a player"""

    def __init__(self, player: Player, house: House):
        self.player: Player = player
        self.house: House = house
        self.condition: dict = {
            LABEL_IMPULSIVE: lambda: True,
            LABEL_CAUTIOUS: lambda: self.house.rent > CAUTIOUS_MIN_RENT,
            LABEL_DEMANDING: lambda: (
                self.player.money - self.house.price > DEMANDING_MIN_LEFTOVER
            ),
            LABEL_UNPREDICTABLE: lambda: random.randint(0, 1) == 0 and self.can_buy(),
        }

    def can_buy(self) -> bool:
        """Checks if current player can buy current house he occupies"""
        return self.house.price <= self.player.money

    def buy(self):
        """Performs the action of buying a house, according to feasibility and player archetype"""
        will_buy: bool = self.can_buy() and self.condition[self.player.archetype]
        if will_buy:
            self.player.spend(self.house.price)
            self.house.owner = self.player
