#Author: Samuel Moore
#Date: 2/10/25
#Description: Q.2 Write a program that takes test grades from the user and returns their average and the letter grade of the average. Use a while loop and make negative number the stop criteria. A>=90 B 80-89 C 70-79 D 60-69 F 59 or less.

total = 0
amount_of_grades = 0

while True:
    grade = int(input('Enter your Grades, or a negative to end: ')) #I tried to have 'grade = int' on the line above but it didnt work
    
    if grade < 0:
        average = total / amount_of_grades 
        break
    
    else:
        grade = int(grade)
        amount_of_grades = amount_of_grades+1
        total = grade + total

letter = int
letter = total
if letter >= 90:
    print('The average grade is A')

elif 89 >= letter >= 80:
    print('The average grade is B')
    
elif 79 >= letter >= 70:
    print('The average grade is C')
    
elif 69 >= letter >= 60:
    print('The average grade is D')
    
elif 59 >= letter:
    print('The average grade is F')