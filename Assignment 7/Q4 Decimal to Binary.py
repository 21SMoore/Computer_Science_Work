#Author: Samuel Moore
#Date: 6/10/25
#Description: Q4 Write a program to convert Decimal to Binary

decimal = input('enter a decimal number: ')
decimal = int(decimal)
binary = ''
while decimal != 0:
    if decimal % 2 == 0:
        binary += '0'

    else:
        decimal -= 1
        binary += '1'

    decimal /= 2
    
reverse_binary = binary[::-1] #found this on google after searching how to reverse a string
print(reverse_binary)