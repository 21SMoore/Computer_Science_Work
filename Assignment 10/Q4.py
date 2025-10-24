#Author: Sam Moore
#Date: 24/10/25
#Assignment 10: Write a Python program to remove characters that have odd index values in a given string.


word = input('Enter a word: ')
word2 = ''
for x in range(len(word)):
    if x % 2 == 0:
        word2 += word[x]
print(word2)