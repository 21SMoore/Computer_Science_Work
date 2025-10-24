#Author: Sam Moore
#Date: 21/10/25
#Description: E1. Write some code to test all the Python string methods given on the python refrence guide.
'''
lowerstring1 = input('Enter a lowercase string: ')
upperstring1 = lowerstring1.upper()
print(upperstring1)


uppercase2 = input('Enter an uppercase string: ')
lowercase2 = uppercase2.upper()
print(lowercase2)


word = input('Enter a word: ')
letter = input('Enter a letter: ')
print(word.count(letter))


word = input('Enter a word: ')
letter = input('Enter a letter: ')
print(word.find(letter))


word = input('Enter a word: ')
letter = input('Enter a letter to replace: ')
newletter = input('Enter a letter to be the replacemet: ')
print(word.replace(letter, newletter))


word = input('Enter a word: ')
if word.islower() == True:
    print(f'{word} is lowercase')
elif word.isupper() == True:
    print(f'{word} is uppercase')
else:
    print(f'{word} is a mix of both')
    

word = input('Enter a word: ')
if word.isalnum() == True:
    print(f'{word} is alphaneumeric')
else:
    print(f'{word} is not alphaneumeric')
    

word = input('Enter a word: ')
if word.isalpha() == True:
    print(f'{word} is alphabetical')
else:
    print(f'{word} is not alphabetic')
    

word = input('Enter a word: ')
if word.isdigit() == True:
    print(f'{word} is a digit')
else:
    print(f'{word} is not a digit')


word = input('Enter a word: ')
letter = input('Enter a letter: ')
print(word.index(letter))

'''
#word = input('Enter a word: ')
#strip = input('Enter what position you want to strip (starts at 0): ')
#strip = int(strip)
#x = word[strip]
#print(word.strip(x))

word = input('Enter a word: ')
x = input('Enter a letter from your word to strip: ')
y = input('Enter a letter from your word to strip: ')
print(word.strip(x, y))