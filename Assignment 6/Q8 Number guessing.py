#Author: Samuel Moore
#Date: 3/10/25
#Description: Q8. Write a program which asks the user to guess a value you have set in your code. The program should tell them if their guess is too high or too low and print a well done message when they guess it correct telling them how many attempts it took

while True:
    number = input('Guess a number: ')
    number = float(number)
    if number == 47:
        print('Well done')
        break
    elif number < 47:
        print('Too low')
    elif number > 47:
        print('Too High')