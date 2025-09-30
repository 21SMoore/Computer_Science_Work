#Author: Samuel Moore.
#Date: 5/9/25
#Description: Q.8 Ask the user to enter 1, 2, or 3. If they enter 1, display the message 'Thank you', if they enter a 2, display 'well done', if they enter a 3, display 'correct'. If they enter anything else display 'error message'

number = int(input('Enter a number: '))
if number == 1:
    print('Thank you')
elif number == 2:
    print('Well done')
elif number == 3:
    print('Correct')
else:
    print('Error message')