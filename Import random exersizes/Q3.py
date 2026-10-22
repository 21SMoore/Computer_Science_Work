#Author: Sam Moore
#Date: 10/2/26
#Description: Randomly choose Heads or Tails. Ask the user to make their choice. If their choice is the same as the randomly selected value display the message ‘you win’, if not, display the message ‘you lose’. Display both the randomly selected and the user input so the user can see the program is fair.

import random

coin = ['heads','tails']
coinflip = random.choice(coin)

guess = input('Guess heads or tails: ')
if guess == coinflip:
    print('Correct!')
else:
    print('Incorrect!')