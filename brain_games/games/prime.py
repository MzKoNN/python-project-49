import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round_data():
    integer = random.randint(1, 100)
    question = f'{integer}'
    number = integer ** 0.5
    if integer < 2:
        n = 'no'
        return question, n
    n = 'yes'
    for i in range(2, int(number) + 1):
        if integer % i == 0:
            n = 'no'
            break
    return question, n