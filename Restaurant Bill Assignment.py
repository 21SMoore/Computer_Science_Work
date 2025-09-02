#Author: Samuel Moore
#1/9/25
#Ask the user for the total price of the bill. Then, ask for the number of diners and output a message saying how much each person must pay.
total_price = int(input('What is the total price of the bill?: '))
people = int(input('How many people ate at your table?: '))
print('The individial price is: ',total_price / people)