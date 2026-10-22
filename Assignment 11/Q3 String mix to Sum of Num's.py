#Assignment 11.
#Author: Sam Moore
#Description: Q3. Write a program to take in a string which is a mixture of characters. Extract all the digits from the string and print their total

string = input('Enter a random sequence of numbers and letters: ')
total = 0
for x in string:
    if x.isdigit():
        total += int(x)
print(total)