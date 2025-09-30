#Author: Samuel Moore
#Date: 9/9/25
#Description: Print the sum of all numbers from 1 to a given number

total = 0
number = int(input('Enter a number: '))
for number2 in range(number + 1):
    total = total + number2
print(total)