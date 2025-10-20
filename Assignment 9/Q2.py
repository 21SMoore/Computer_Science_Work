#Author: Samuel Moore
#Date: 17/10/25
#Description: Assignment 9: Q2 Ask the user to enter their first name and then their surname. Join them together with a space between and then display their full name and the length of their full name

fname = input('Enter your first name: ')
sname = input('Enter your surname: ')

letter = len(fname + ' ' + sname)

print(fname + ' ' + sname)
print(letter)