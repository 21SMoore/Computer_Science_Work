#Author: Samuel Moore
#Date 9/10/25
#Description: Assignment 8. Q14 Write a program to take N (N.20) as an input from the user. print numbers from 11 to N. When the number is a multiple of 3, print "tipsy", when it is a multiple of 7, print "topsy". When it is a multiple of both, print "TipsyTopsy"

N = input('Enter a number under 20: ')
N = int(N)

if N > 20:
    for x in range(11,N + 1):
        print(x)
    
    if N % 3 == 0 and N % 7 == 0:
        print('TipsyTopsy')
        
    elif N % 3 == 0:
        print('Tipsy')
    
    elif N % 7 ==0:
        print('Topsy')
        
else:
    print('Number is under 20, please try again.')