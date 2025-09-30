#Author: Samuel Moore
#Date: 11/9/25
#Description: Print a multiplication table of a given number.

total = 0
number = int(input('Enter a number to see its multiplication table: '))
for number2 in range(1,13):
    total = number * number2
    print(f'{number}x{number2}={total}')