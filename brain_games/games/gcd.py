#!/usr/bin/env python3
import random
TASK = 'Find the greatest common divisor of given numbers.'


def generate_round():
    a = random.randrange(1, 100)
    b = random.randrange(1, 100)
    sequence = [i for i in range(1, max(a, b))]
    answer = max(list(filter(lambda x: a % x == 0 and b % x == 0, sequence)))
    question = f'Question: {a} {b}'
    if a == b:
        answer = a
    return question, str(answer)
