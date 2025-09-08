#Author: Samuel Moore
#Date: 8/9/25
#Description: 5. Set a variable called total to 0. Ask the user to enter five numbers. After each input ask if they wish to add that number to the total. If they do, add the number else do not add the number. When they have entered five numbers, display the total.

total = 0
for i in range(5):
    number = int(input('Enter a number: '))
    add = input('Do you want to add that to the total?: ')
    if add == 'yes' or add == 'Yes':
        total = total + number
    else:
        continue
print(total)