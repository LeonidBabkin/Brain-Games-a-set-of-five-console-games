#!/usr/bin/env python3
import random
TASK = 'What number is missing in the progression?'


def generate_progression():
    a = random.randrange(1, 50)
    b = random.randrange(100, 1000)
    substitution = random.randrange(3, 10)
    step = random.randrange(1, substitution)
    sequence = [i for i in range(min(a, b), max(a, b), step)]
    return sequence, substitution


def generate_round():
    sequence, substitution = generate_progression()
    answer = sequence[substitution]
    sequence[substitution] = '..'
    sequence = sequence[0:10]
    sec = list(map(lambda x: str(x), sequence))
    sec = " ".join(sec)
    question = f'Question: {sec}'
    return question, str(answer)
