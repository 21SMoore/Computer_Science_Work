#Author: Sam Moore
#Date: 1/30/26
#Description# Hangman



HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

 
print(f'Welcome to hangman. Please save a life guessing the correct word.')

import random

tries = 0
word = words[random.randint(0, len(words))]
wincondition = 0

#blanks
underscore = []
track = 0#set track to zero after each time it increases

#guessed letters
guesses = []

#gives blank spaces the same size of the word
for x in word:
    underscore += '_'




while True:#makes the game rerun for each guess till you run out of tries
    if tries == 7:
        print('You ran out of guesses. =(')
        break
        
        
    print('\nWord:'," ".join(underscore))#puts a space between each underscore
    print(HANGMANPICS[tries])#visual that updates per wrong guess

    #guessing
    guess = input('\nGuess the letter: ')
    if guess.isalpha():#checks if guess is a letter
        print('\n\n\n\n\n')
        #if letter guessed before
        if guess in guesses or guess in underscore:
            print('You have already guessed this letter')
            continue#returns to the start of the while true loop
        
        #if letter is long
        if len(guess) > 1:
            print('Guess 1 letter please')
            continue#returns to the start of the while true loop
            
        if guess in word:
            for x in word:
                if guess == x:
                    underscore[track] = guess#replaces the underscore at [track] position with the guessed letter
                    print(f'{guess} is in the word. ')
                    wincondition += 1 
                track += 1#moves up to the next index
            track = 0
        
        #increases tries if youve guessed wrong
        elif guess not in word:
            guesses += guess
            print(f'{guess} is not in the word.')
            tries += 1
    
        #shows each wrong guess
        print('You have guessed: ', ', '.join(guesses))
        
    #if guess isnt valid
    else:    
        print('Please enter a valid letter.')
        continue#returns to the start of the while true loop
    
    #win
    if wincondition == len(word):
        print('YOU WIN!!!!!')
        break

