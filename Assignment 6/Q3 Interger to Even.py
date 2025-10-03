#Author: Samuel Moore
#Date: 2/10/25
#Description: Q.3 Write a program that takes an interger number and outputs all the even numbers starting from 0 to the number. (hint use % and use continue)


number = int(input('Enter a number: '))

for even in range (0, number + 1):
    if even % 2 == 1:
        continue
    print(even)