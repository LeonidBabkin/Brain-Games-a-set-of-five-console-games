#!/usr/bin/env python3
import random
TASK = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def generate_round():
    number = random.randrange(1, 15)
    question = f'Question: {number}'
    if number % 2 == 1:
        answer = 'no'
    else:
        answer = 'yes'

    return question, answer
