#Author: Samuel Moore
#Date: 6/10/25
#Description: Q3 Write a program to convert Binary to Decimal

binary = input('Enter a Binary number: ')

power = 0
number = 0
total = 0

for n in binary:
    power += 1

for n in binary:
    n_ = int(n) #n_ is the variable i made an int for n because you cant make n an int
    n_ = n_ * 2
    power -= 1 # because i add +1 to power, its 1 power too high
    number = n_ ** power
    total += number
    
print(total)