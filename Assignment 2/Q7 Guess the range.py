#Author: Samuel Moore.
#Date: 5/9/25
#Description: 7. Ask the user to enter a number. If it is under 10, display the message 'too low', if their number is between 10 and 20 display 'correct', otherwise display 'too high'

number = int(input('Enter a number: '))
if number<10:
    print('Too low')
if number>9 and number<21:
    print('Correct')
if number>20:
    print('Too high')