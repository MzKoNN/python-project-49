import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def generate_round_data():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    if a < b:
        a, b = b, a
    if b == 0:
        GCD = a
    elif b != 0:
        while b != 0:
            new_a = b
            b = a % b
            a = new_a
            GCD = new_a
    return question, str(GCD)