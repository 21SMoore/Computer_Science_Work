#Assignment 11.
#Author: Sam Moore
#Description: Q1. Write a program to reverse a string using: A for loop, A while loop, slicing.

string = input('Enter a string: ')
word = ''

#for loop
for x in string:
    word = x + words
print(word)

#while loop
index = 0
while True:
    if len(word) < len(string):
        y = string[index]
        word = y + word
        index += 1 #index to make y move onwards in the word
    else:
        break
print(word)

print(string[::-1])