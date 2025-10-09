#Author: Samuel Moore
#Date: 6/10/25
#Description: Write a program to check if a number is an Armstrong number. An Armstrong number is a number equal to the sum of the cube of it’s digits.
#Example: 153 is an Armstrong number as 153 = 1

total = 0
number = input('Enter a number: ')
amount = 0

for n in number:
    amount += 1
    
for n in number:
    n = int(n) 
    power = n ** amount
    total += power
    
number = int(number)

if total == number:
    print(f'{number} is an Armstrong number.')

else:
    print(f'{number} is not an Armstrong number')