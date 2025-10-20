#Author: Samuel Moore
#Date 9/10/25
#Description: Assignment 8. Q13 Write a program to take an integer as an input and check whether it ends with 4 or 8. If it ends with 4, print "ends with 4", if it ends with 8, print "ends with 8", otherwise print "ends with neither".

number = input('Enter a number: ')

reverse_number = number[::-1] #use the [::-1] to reverse the number and find the first one

if '4' in number:
    if reverse_number.index('4') == 0:
        print('Ends with 4')
    
elif '8' in number:
    if reverse_number.index('8') == 0:
        print('Ends with 8')
    
else:
    print('Ends with neither')