#Author: Samuel Moore
#Date 9/10/25
#Description: Assignment 8. Q16 Write a program to input N numbers and then print the second largest number.

list = []
while True:
    n = input('Enter a number to add, or a letter to break: ')
    if n.isdigit():
        n=int(n)
        list.append(n)
        list.sort(reverse = True)
    else:
        print(list[1])
        break