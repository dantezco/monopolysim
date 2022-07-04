"""Main module for this project"""
from src.simulation import Simulation


def main():
    """Main point of entry"""
    simulation: Simulation = Simulation()
    return simulation.run()
