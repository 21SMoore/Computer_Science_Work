#Author: Samuel Moore
#Date: 8/9/25
#Description: 2. Ask the user to enter their name and their number. Display their name the given number of times.

name = input('enter your name: ')
number = int(input('Enter how many times you want to repeat it: '))
for i in range(number):
    print(name, end=', ')


