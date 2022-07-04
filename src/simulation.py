"""
Module for the simulation code, for running multiple games and gathering their statistics
"""

from src.constants import (
    AMOUNT_SIMULATIONS,
    LABEL_CAUTIOUS,
    LABEL_DEMANDING,
    LABEL_IMPULSIVE,
    LABEL_UNPREDICTABLE,
)
from src.game import Game
from src.log import get_logger
from src.players import Player

LOGGER = get_logger(__name__)


class Simulation:
    """Runs multiple games and calculates statistics based on their results"""

    @staticmethod
    def find_most_wins(wins: dict) -> str:
        """Returns the player that has the most wins"""
        scores: list = list(wins.items())
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[0][0]

    @staticmethod
    def calculate_win_percentages(wins: dict):
        """Calulates the percentage of wins per player,
        relative to the amount of games where there was a winner"""
        wins_absolutes: int = sum(win[1] for win in wins.items())
        LOGGER.debug("Number of games where a player won: %s", wins_absolutes)
        return {player: (wins[player] / wins_absolutes) * 100 for player in wins}

    def run(self):
        """Runs all simulations, gather statistics"""
        game_lengths: list = []
        wins: dict = {
            LABEL_IMPULSIVE: 0,
            LABEL_CAUTIOUS: 0,
            LABEL_DEMANDING: 0,
            LABEL_UNPREDICTABLE: 0,
        }
        for _ in range(AMOUNT_SIMULATIONS):
            game: Game = Game()
            winner: Player = game.run()
            game_lengths.append(game.turn_counter)
            wins[winner.archetype] += 1
        return self.gather_statistics(game_lengths=game_lengths, wins=wins)

    def gather_statistics(self, game_lengths: list, wins: dict) -> dict:
        """Calculates statistics based on game results"""
        statistics: dict = {
            "amount of timeouts": game_lengths.count(1000),
            "average amount of turns": round(sum(game_lengths) / len(game_lengths)),
            "players' victory percentages": self.calculate_win_percentages(wins=wins),
            "player with most victories": self.find_most_wins(wins=wins),
        }
        return statistics
