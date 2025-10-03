#Author: Samuel Moore
#Date: 2/10/25
#Description: Q.6 Write a program which takes in a numbers from the user. It should continue taking in numbers until the total of all the numbers entered is greater than 50.

total = 0
while total <= 50:
    number = input('Enter a number: ')
    number = float(number)
    total = total + number
    if total >= 50:
        break