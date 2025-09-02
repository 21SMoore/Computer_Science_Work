#Author: Samuel Moore
#Date 1/9/25
#7. Write a python program that accepts marks in 5 subjects and outputs average marks.

mark1 = int(input('Type your first mark: '))
mark2 = int(input('Type your second mark: '))
mark3 = int(input('Type your third mark: '))
mark4 = int(input('Type your fourth mark: '))
mark5 = int(input('Type your fifth mark: '))

total = int(mark1 + mark2 + mark3 + mark4 + mark5)
average = total/5

print('Your average is:',average)