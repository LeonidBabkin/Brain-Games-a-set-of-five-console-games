#!/usr/bin/env python3
import random
TASK = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def calc_func():
    number = random.randrange(1, 15)
    question = f'Question: {number}'
    if number % 2 == 1:
        v = 'no'
    else:
        v = 'yes'

    return question, v


