#!/usr/bin/env python3
from brain_games.engine import start  # import a function
from brain_games.games import arithmasy  # import the whole module


def main():
    start(arithmasy)  # call the whole module named calc.py


if __name__ == '__main__':
    main()
