#Assignment 11.
#Author: Sam Moore
#Description: Q5. Write a program which asks the user to enter a string of digits, and a step size. Go through the string and add the first number plus all the numebrs at the step size.

total = 0
numbers = input('Enter a string of digits: ')
step = input('Enter a step size: ')
step = int(step)

for x in numbers[::step]:
    x = int(x)
    total += x
print(total)