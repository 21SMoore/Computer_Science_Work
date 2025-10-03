#Author: Samuel Moore
#Date: 2/10/25
#Description: Q.5 Write a program that prints 1 to n squared using a while loop. It should stop the while loop if the iteration count reaches 50 (hint use break)

n = input('Enter a number: ')
n = int(n)
number = 0
nsq = n**2

while number < nsq:
    number = number + 1
    print(number)
    if number == 50:
        break