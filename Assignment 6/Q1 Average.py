#Author: Samuel Moore
#Date: 2/10/25
#Description: Q.1 Write a program that takes intergers from the user and returs the average. Use a while loop and make an empty string the stop criteria.

total = 0
amount_of_numbers = 0

while True:
    numbers = input('Enter a number, or nothing to end: ')
    if numbers == '':
        average = total / amount_of_numbers
        print(f'The average is {average}')
        break
    else:
        numbers = int(numbers)
        amount_of_numbers = amount_of_numbers+1
        total = numbers + total