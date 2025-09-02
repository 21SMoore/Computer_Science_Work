#Author: Samuel Moore
#1/9/25
#Ask the user for their name and their age. Calculate their age next year and then display the message: Hello <user_name>, next year you will be <new_age> years old.
name = input('What is your name?: ')
age = int(input('What is your age?: '))
new_age = int(age + 1)
print(f'Hello {name}, next year you will be {new_age} years old.')