#!/usr/bin/env python3
from random import randrange
TASK = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def calc_func():
    num = randrange(1, 1000)
    question = f'Question: {num}'
    for i in range(2, num):
        if (num % i) == 0:
            answer = 'no'
            return question, str(answer)
        answer = 'yes'
        return question, str(answer)
