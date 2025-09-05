#Author: Samuel Moore
#Date: 4/9/25
#Description: 3. Ask the user to enter a number between 10 and 20 inclusive. If they enter a number in this range display the 'Thank you.'. Otherwise, display the message 'incorrect value entered.'.

number = int(input('Enter a number between 10 and 20: '))

if (number > 10) and (number < 20):
    print(f'{number} is in the range.')

if(number> 20) or (number < 10):
    print(f'{number} is not in the range.')
    
else:
    print(f'{number} is in the range.')