#!/usr/bin/env python3
from brain_games.engine import gamestart_func  # import a function
from brain_games.games import prime  # import the whole game module


def main():
    gamestart_func(prime)  # call the whole game module named calc.py


if __name__ == '__main__':
    main()
