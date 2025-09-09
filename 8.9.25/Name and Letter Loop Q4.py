#Author: Samuel Moore
#Date: 8/9/25
#Description: 4. Ask the user to enter their name and a number. Display each letter of their name on a seperate line and repeat this for the number of times they entered.

name = input('Enter your name: ')
number = int(input('Enter your number: '))
for s in range(number):
    for letter in name:
        print(letter)
