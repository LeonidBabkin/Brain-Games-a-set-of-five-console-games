#!/usr/bin/env python3
from brain_games.engine import start  # import a function
from brain_games.games import progression  # import the whole game module


def main():
    start(progression)  # call the whole game module named calc.py


if __name__ == '__main__':
    main()
