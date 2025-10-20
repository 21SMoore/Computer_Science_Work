#Author: Samuel Moore
#Date 9/10/25
#Description: Assignment 8. Q18 Write a complete Python program to do the following: (i) read an integer X. (ii) determine the number of digits n in X. (iii) form an integer Y that has the number of digits n at tens place and the most significant digit of X at ones place. (iv) output Y

x = input('Enter a number: ')
count = 0

for num in x:
    count += 1
    
z = x[0]
z = int(z)

y = count * 10 + z
print(y)