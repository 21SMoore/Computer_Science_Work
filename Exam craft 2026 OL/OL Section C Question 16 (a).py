#Question16_A_OL
#Enter your name here: Sam Moore

print("Welcome to the Step Tracker App!")

name = input("Enter your name: ")
steps_today = int(input("Enter the number of steps you walked today: ")) #this is where the user enters the number of steps.


if steps_today >=10000:
    print("Well done",name,"! You reached your goal.")

elif steps_today < 10000 and steps_today > 5000:
    print("Good effort, almost there!",name)
    
elif steps_today < 5000:
    print("try to be more active today!",name)

elif steps_today < 0:
    print("The number cannot be negative")