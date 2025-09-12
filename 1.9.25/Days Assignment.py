#Author: Samuel Moore
#1/9/25
#Ask the user to enter a random number of days. Output how many hours, minutes and seconds are in the given number of days.

day = float(input('Enter a random number of days: '))

hour = (day * 24)
minute = (hour * 60)
second = (minute * 60)

print(day,hour,minute,second)

