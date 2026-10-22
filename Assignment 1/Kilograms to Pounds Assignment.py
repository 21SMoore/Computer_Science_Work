#Author: Samuel Moore
#1/9/25
#There are 2.204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it pounds. Display the result: There are <number_of_pounds> in <number_of_kilograms_entered_by_the_user>

kilogram = int(input('Enter a weight in kilograms: '))
pound = (kilogram * 2.204)
print(f'There are {pound} in {kilogram} kilograms')