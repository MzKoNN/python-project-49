import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round_data():
    step = random.randint(1, 10)
    start = random.randint(1, 30)
    index = 0
    progression = []
    while index < 10:
        currentElement = start + index * step
        index += 1
        progression.append(currentElement)
    hidden_index = random.randint(0, 9)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    question = " ".join(map(str, progression))
    quest = f'{question}'
    return quest, str(hidden_value)