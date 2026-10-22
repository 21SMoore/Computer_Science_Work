#Author: Sam Moore
#Date: 10/2/26
#Description:
#Write code to ask the player to enter their name.
#Create a variable called luckey_number and assign its value to 5,
#Create a variable called computer_die_roll and assign it a random integer between 1 and 6 inclusive,
#Print a message showing the value the computer rolled

import random


computer_die_roll = random.randint(1,6)#initialize computer number

print('Welcome to my dice game!!')
name = input('Please enter your name: ')
lucky_number = input('Please select a luckey number between 1 and 6: ')
lucky_number = int(lucky_number)


print(f"{name}'s lucky number was: {lucky_number}")
print(f'The computer rolled: {computer_die_roll}')

if lucky_number == computer_die_roll:
    print('You guessed correct, well done!')

if lucky_number < computer_die_roll:
    print('You guessed too low!')
    
if lucky_number > computer_die_roll:
    print('You guessed too high!')