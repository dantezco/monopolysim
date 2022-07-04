"""
Main module for the game application
"""
import random
from typing import Optional

from src.actions import Buy
from src.board import House, board
from src.constants import MAX_TURNS, WENT_FULL_BOARD_VALUE
from src.log import get_logger
from src.players import Player, init_players

LOGGER = get_logger(__name__)


class Game:
    """Control class for the game of simplified monopoly"""

    def __init__(self):
        self.players: list = init_players()
        self.player_pointer: int = 0
        self.current_player: Optional[Player, None] = None
        self.turn_counter: int = 0

    def get_current_player(self) -> None:
        """Moves the game pointer to the player up for the current turn"""
        self.player_pointer: int = (self.player_pointer + 1) % len(self.players)
        self.current_player: Player = self.players[self.player_pointer]

    def move_player(self) -> None:
        """Moves the player to his new position
        and determines if a full round around the board was done"""
        old_position: int = self.current_player.position
        self.current_player.position = (
            self.current_player.position + random.randint(1, 6)
        ) % len(board)
        LOGGER.debug(
            "%s is now on position %s",
            self.current_player.archetype,
            self.current_player.position,
        )

        if old_position > self.current_player.position:
            self.current_player.earn(value=WENT_FULL_BOARD_VALUE)
            LOGGER.debug(
                "%s has earned %s", self.current_player.archetype, WENT_FULL_BOARD_VALUE
            )

    @staticmethod
    def release_houses(player: Player) -> None:
        """Removes all ownership from houses of losing player"""
        for house in board:
            if house.owner == player:
                house.remove_owner()
                LOGGER.debug("Released house %s from %s", house.name, player.archetype)

    def act_on_position(self) -> None:
        """Performs relevant action on position current player occupies"""
        house: House = board[self.current_player.position]
        if house.has_owner():
            self.current_player.spend(value=house.rent)
            LOGGER.debug(
                "%s payed %s in rent", self.current_player.archetype, house.rent
            )
            if self.current_player.money < 0:
                self.release_houses(player=self.current_player)
                self.players.remove(self.current_player)
                LOGGER.debug(
                    "%s lost with balance %s. Players left: %s",
                    self.current_player.archetype,
                    self.current_player.money,
                    [player.archetype for player in self.players],
                )
        else:
            Buy(player=self.current_player, house=house).buy()
            LOGGER.debug("%s bought %s", self.current_player.archetype, house.name)

    def take_turn(self) -> None:
        """Performs all actions included in a turn"""
        self.get_current_player()
        self.move_player()
        self.act_on_position()

    def is_game_ended(self) -> bool:
        """Checks game for end conditions"""
        took_too_long: bool = self.turn_counter >= MAX_TURNS
        one_player_won: bool = len(self.players) < 2

        game_ended: bool = took_too_long or one_player_won
        LOGGER.debug("Game has ended? %s", game_ended)
        return game_ended

    def run(self) -> Player:
        """Main loop of the game"""
        while not self.is_game_ended():
            self.turn_counter += 1
            LOGGER.debug(
                "TURN: %s =====================================", self.turn_counter
            )

            self.take_turn()
        winner: Player = self.players[0]
        return winner
