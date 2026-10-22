#Author: Sam Moore
#Date: 10/2/26
#Description:Make a maths quiz by randomly generating two whole numbers and an operator (+, -, *, /). Ask the user to enter the answer. Each time they get the answer correct add 1 point to their score. The program should run until the user enters q to quit

import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)
operator = ['+', '-', '*', '//']
operatorrandom = random.choice(operator)

while True:
    answer = input(f'Give the answer for this question: {number1} {operatorrandom} {number2} (enter q to exit) : ')
    
    #exit
    if answer == 'q':
        break
    
    #+
    if operatorrandom == '+':
        if number1 + number2 == answer:
            print('Correct!')
            break
        else:
            print('Incorrect! Try again.')
    
    #-
    if operatorrandom == '-':
        if number1 - number2 == answer:
            print('Correct!')
            break
        else:
            print('Incorrect! Try again.')
    
    #*
    if operatorrandom == '*':
        if number1 * number2 == answer:
            print('Correct!')
            break
        else:
            print('Incorrect! Try again.')            
    
    #/
    if operatorrandom == '//':
        if number1 // number2 == answer:
            print('Correct!')
            break
        else:
            print('Incorrect! Try again.')
    
    print(' ')