#Author: Sam Moore
#Date: 10/2/26
#Description:Randomly pick a number between 1 and 100 inclusive. Ask the user to guess the number, they can keep guessing until they get it correct or until they have used 7 guesses. Print a suitable success and failure message.

import random

range = random.randint(1,100)

tries = 0
b = 7

while tries != 7:
    print(f'You have {b} tries.')
    guess = input('Guess a number between 1 and 100 inclusive: ')
    guess = int(guess)
    if guess == range:
        print('Correct!')
        break
    else:
        print('Incorrect!')
        tries +=1
        b -= 1
if tries == 7:
    print('You have failed')
else:
    print('You Win')