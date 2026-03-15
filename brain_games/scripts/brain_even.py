import random

import prompt

from brain_games.cli import welcome_user


def get_random_number():
    return random.randint(1, 100)


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = get_random_number()
        if number % 2 == 0:
            n = 'yes'
        else:
            n = 'no'
        print(f'Question: {number}')
        name_number = prompt.string('Your answer: ')
        if n == name_number:
            print('Correct!')
            counter += 1
        else:
            print(
                f"'{name_number}' is wrong answer ;(. "
                f"Correct answer was '{n}'"
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()