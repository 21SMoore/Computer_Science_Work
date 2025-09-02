#Author:Samuel Moore
#Date: 1/9/25
#Description: Ask the user to enter three numbers. Add toghether the first two and store this answer in a variable.
#Then multiply this result by the third. Display the answer as: The answer is: <calculated result>

number_one = input('Enter your first number: ')
number_two = input('Enter your second number: ')
number_three = input('Enter your third number: ')

number_one = int(number_one)
number_two = int(number_two)
number_three = int(number_three)

answer_1 = (number_one + number_two)
answer_2 = (answer_1 * number_three)
print('The answer is:',answer_2)