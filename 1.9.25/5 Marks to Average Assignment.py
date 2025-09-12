#Author: Samuel Moore
#Date 1/9/25
#7. Write a python program that accepts marks in 5 subjects and outputs average marks.

mark1 = float(input('Type your first mark: '))
mark2 = float(input('Type your second mark: '))
mark3 = float(input('Type your third mark: '))
mark4 = float(input('Type your fourth mark: '))
mark5 = float(input('Type your fifth mark: '))

total = float(mark1 + mark2 + mark3 + mark4 + mark5)
average = total/5

print('Your average is:',average)

