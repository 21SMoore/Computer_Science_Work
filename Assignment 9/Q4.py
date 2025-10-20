#Author: Samuel Moore
#Date: 17/10/25
#Description: Assignment 9: Q4 Write a program to count the number of times a character occurs in the given string. The string and the character should be input by the user.

total = 0
word = input('Enter a word: ')
letter = input('Enter a letter: ')

for character in word:
    if character == letter:
        total += 1
    

print(total)