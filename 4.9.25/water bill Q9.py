#Author: Samuel Moore.
#Date: 5/9/25
#Description: Q.9 Write a program to display the total water bill charges for a month given the number of units consumed. Your calculation should be based on the following rates: 5 cent a unit for the first 100 units, 10 cents a unit for the next 150 units, 20 cent for any over 250

waterused = int(input('How much water have you consumed?: '))
if waterused == 100 or waterused<100:
    print(f'Your water bill is: {waterused * 5} cent')
elif waterused>100 or waterused<151:
    waterused2=waterused-100
    print(f'Your water bill is: {waterused2 * 10+500} cent')
elif waterused>150:
    waterused2=waterused-250
    print(f'Your water bill is: {waterused2 * 20+2000} cent')