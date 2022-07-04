"""
This module contains logic for the game board
"""

from typing import Optional

from src.players import Player


class House:
    """Encapsulates all the attributes of the house"""

    def __init__(self, name: str, value: int, rent: int) -> None:
        self.name: str = name
        self.price: int = value
        self.rent: int = rent
        self.owner: Optional[Player, None] = None

    def has_owner(self) -> bool:
        """Checks if the house is currently owned by a player"""
        return self.owner is not None

    def remove_owner(self) -> None:
        """Makes the house unowned"""
        self.owner = None


board = [
    House("Zerope", 500, 50),
    House("Onett", 200, 30),
    House("Twoson", 130, 80),
    House("Threed", 120, 10),
    House("Fourside", 410, 100),
    House("Fivern", 280, 80),
    House("Sixous", 220, 60),
    House("Seveno", 470, 70),
    House("Eightel", 160, 40),
    House("Ninelia", 290, 90),
    House("Tenis", 240, 100),
    House("Elevenal", 350, 20),
    House("Twelvepy", 310, 10),
    House("Thirteenar", 110, 70),
    House("Fourteenal", 1000, 130),
    House("Fifteenio", 3600, 1200),
    House("Sixteenos", 150, 90),
    House("Seventeenon", 280, 70),
    House("Eighteenoo", 480, 40),
    House("Nineteenely", 310, 30),
]
