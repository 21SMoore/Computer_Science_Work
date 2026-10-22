#Assignment 12.
#Author: Sam Moore
#Description: Q10. Write a program to convert a given number into equivalent Roman number.
#From the given number, pick successive digits, using %10 and /10 to gather the digits from rght to left
#(store its value as a string)
number = input('Enter a number: ')
number = int(number)

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000