#Author: Samuel Moore
#Date: 2/10/25
#Description: Q.4 Write a program that prints from 1 to n using a while loop, it should skip every multiple of 5. (Hint use % and continue)

number = int(input('Enter a number: '))

num = 0
while num <= number:
    num = num + 1
    if num % 5 == 0:
        continue
    print(num)