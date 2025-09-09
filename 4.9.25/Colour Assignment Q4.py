#Author: Samuel Moore
#Date: 4/9/25
#Description: 4. Ask the user to enter their favourite colour. If they enter 'red', 'RED', or 'Red' - display the message 'I like red too'. Otherwise, display the message 'I dont like the colour {colour}, I prefer red.'

colour = input('What is your favourite colour?: ')

if (colour == "red") or (colour == "Red") or (colour == "RED"):
    print('I like red too.')
    
else:
    print(f'I dont like {colour}, I prefer red.')
