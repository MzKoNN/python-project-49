import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def generate_round_data():
    integer = random.randint(1, 100)
    question = f'{integer}'
    if integer < 2:
        n = 'no'
    elif integer == 2:
        n = 'yes'
    elif integer % 2 == 0:
        n = 'no'
    else:
        n = 'yes'
    return question, n