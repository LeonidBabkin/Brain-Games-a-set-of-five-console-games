#!/usr/bin/env python3
from random import randrange
TASK = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'



def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def generate_round():
    num = randrange(1, 100)
    question = f'Question: {num}'
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer
