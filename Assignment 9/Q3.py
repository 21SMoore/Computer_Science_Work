#Author: Samuel Moore
#Date: 17/10/25
#Description: Assignment 9: Q3 Ask the user to enter a word and print the word madified as follows:
#if the fisrt letter of the word is a vowel, add 'way' to the end. So, if the user enters 'apple' it should output 'appleway'
#if the first letter of the word is a consonant, move the first letter to the end and add 'ay'. So, if the user enters 'pear' it should output as 'earpay'

word = input('Enter a word: ')

if word[0] in 'aeoiu':
    print(word + 'way')

else:
    print(word[1:] + word[0] + 'ay')