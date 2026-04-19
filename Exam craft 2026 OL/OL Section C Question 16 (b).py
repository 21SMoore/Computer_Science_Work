#Question16_B_OL
#Enter your name here: Sam Moore

day = 0
weekly_steps = []

#steps input
print("Welcome to my weekly step tracker!")
while day < 7:
    steps = input("Enter your steps for each day of the week: ")
    steps = int(steps)
    weekly_steps.append(steps)
    day += 1

#steps output
print("The list of steps is:",weekly_steps)

total_steps = weekly_steps[0] + weekly_steps[1] + weekly_steps[2] + weekly_steps[3] + weekly_steps[4] + weekly_steps[5] + weekly_steps[6]
print("The total steps is:",total_steps)

average_steps = total_steps / 7
print("The average number of steps is:",average_steps)

print("The largest number of steps you took this week was:",max(weekly_steps))

print("The smallest number of steps you took this week was:",min(weekly_steps))