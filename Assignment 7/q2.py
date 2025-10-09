#Author: Samuel Moore
#Date: 6/10/25
#Description: Write a program to enter numbers until the user enters 0. Then it should print the count of the positive and negative numbers entered. You can assume all input is numeric.

amount_positive = 0
amount_negative = 0

while True:
    numbers = input('Enter a number or "0" to end: ')
    numbers = int(numbers)
    if numbers == 0:
        print(amount_positive, amount_negative)
        break
    elif numbers > 0: #positive
        amount_positive += 1
        
    elif numbers < 0: #negative
        amount_negative += 1