#!/usr/bin/env python3
from brain_games.engine import gamestart_func
from brain_games.games import great_div


def main():
    gamestart_func(great_div)


if __name__ == '__main__':
    main()
