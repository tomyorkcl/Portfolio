# Created by: Tomas Contreras, student from BYU Idaho

import random

def main():

    random = random_number()

    attempt_number = 0
    #max number of attempts permited
    max_attempts = 10

    while attempt_number < max_attempts:

        attempt_number += 1

        try:
            guess = int(input('Introduce your number: '))

        except ValueError:
            print('Please introduce a valid number.')
            continue

        if guess < random:
            print('The number is too low. Try again.')
        
        elif guess > random:
            print('The number is too high. Try again.')

        else:
            print(f'Congratulations! you guess the number in {attempt_number} attempts.')
            break

        if attempt_number == max_attempts:
            print(f'Sorry! the secret number was {random}. You lose your {max_attempts} attempts.')


def random_number():
    #Generate a random number between 1 - 20.
    secret_number = random.randint(1, 20)
    return secret_number


if __name__ == "__main__":
    main()