#!/usr/bin/env python3
from random import randrange
TASK = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def calc_func():
    num = randrange(1, 100)
    question = f'Question: {num}'
    for num in range(1, num + 1):
        for i in range(2, num):
            if (num % i) == 0:
                answer = 'no'
                break
        else:
            answer = 'yes'
    return question, answer
