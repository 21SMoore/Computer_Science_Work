#Author: Samuel Moore
#Date 9/10/25
#Description: Assignment 8. Q15 Write a short program to find the largest number of a list of numbers entered through keyboard.

list = []
while True:
    n = input('Enter a number to add, or a letter to break: ')
    if n.isdigit():
        n=int(n)
        list.append(n)
        list.sort(reverse = True)
    else:
        print(list)
        break