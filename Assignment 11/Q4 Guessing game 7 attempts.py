#Assignment 11.
#Author: Sam Moore
#Description: Q4. Write a program which asks the user to guess a number between 1 and 100 inclusive. You can hardcode the number they are trying to guess. Prompt the user if they are too high or too low. they can have no more than 7 attempts. If they use more than 7 print 'Game Over' and tell them the answer.
success = False
number = 50
attempts = '1234567' #making a 7 letter string for 7 attempts
for x in attempts:
    guess = input('Guess a number between 1 and 100: ')
    guess = int(guess)
    
    if guess > 50:
        print('Too High')
    elif guess < 50:
        print('Too Low')
    elif guess == 50:
        print('Well done')
        success = True
        break
    
if not sucsess:
    print('Game Over')