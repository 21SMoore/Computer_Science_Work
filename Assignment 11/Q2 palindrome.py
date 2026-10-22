#Assignment 11.
#Author: Sam Moore
#Description: Q2. Write a program to check if a string is a palindrome. A palindrome is a word or string that reads the same backwards and forwards. For example: racecar;rotator

word = input('Enter a word: ')
if word == word[::-1]:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')