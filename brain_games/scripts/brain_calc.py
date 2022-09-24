#!/usr/bin/env python3
from brain_games.engine import gamestart_func  # import a function
from brain_games.games import calc  # import the whole module


def main():
    gamestart_func(calc)  # call the whole module named calc.py


if __name__ == '__main__':
    main()
