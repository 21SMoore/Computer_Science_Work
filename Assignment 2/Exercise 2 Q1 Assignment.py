#Author: Samuel Moore
#Date: 4/9/25
#Description: 1. Ask the iser to input two numbers. Display the two numbers with the least of the two numbers printed first. Take it that the two numbers are never equal.

a = int(input('Type a random number: '))
b = int(input('Type a second random number: '))

if (a>b):
    print(f'{a} is greater than {b}')

elif (a<b):
    print(f'{b} is greater than {a}')
    
elif (a==b):
    print(f'{a} and {b} are equal')