#Author: Samuel Moore
#Date 9/10/25
#Description: Assignment 8. 19: Write a python program to print every integer between 1 and n divisible by m. Also report whether the number that is divisible by m is even or odd

number = 0

n = input('Enter a number: ')
n = int(n)

m = input('Enter another number: ')
m = int(m)

for x in range (1, n):
    if x % m == 0:
        print(x)
        
if n % 2 != 0:
    print('First number is odd')

elif n % 2 == 0:

    print('First number is even')

#im still working on Q20
