#Author: Samuel Moore
#Date: 4/9/25
#Description: 2. Ask the user to enter a number under 20. If they enter a number that is 20 or over, display the message 'Too High'. Otherwise, display the message 'Thank you: '.

number = float(input('Enter a number under 20: '))

if (number<20):
    print('Thank You!')

if (number>20):
    print(f'{number} is too high')

if (number == 20):
    print(f'{number} is too high')


