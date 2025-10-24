#Author: Sam Moore
#Date: 24/10/25
#Assignment 10: Q3. Create a string where all occurances of its first char have been changed to $, except for the first character itself

word = input('Enter a string: ')
word2 = word[1:].replace(word[0], '$')
print(word[0] + word2)