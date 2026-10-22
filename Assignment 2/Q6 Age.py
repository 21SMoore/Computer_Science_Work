#Author: Samuel Moore.
#Date: 5/9/25
#Description: 6. Ask the user's age. If they are 18 or over, display the message 'You can vote'. If they are aged 17, display the message ' you can learn to drive'. If they are 16 display the message 'you can buy a lottery ticket'. If they are under 16 display the message 'you can go trick or treating'

age = int(input('What is your age?: '))
if age == 18:
    print('You can vote.')

elif age == 17:
    print('You can learn to drive')
    
elif age == 16:
    print('You can buy a lottery ticket')
    
if age<16:
    print('You can go Trick or Treating')

if age>18:
    print('You can vote.')