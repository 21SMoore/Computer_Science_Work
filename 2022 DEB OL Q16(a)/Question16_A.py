# Question 16(a) 
# Name and School: Sam Moore

import random

while True:
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age = input("Enter your age: ")
    age = int(age)
    eircode = input("Enter your Eircode: ")
    trial = input("Do you agree to enrol in a vaccine trial? ")
    odd = ["1", "3", "5", "7", "9"]
    supervaccine = ["A", "B", "C"]

    
    print("Hello", f_name, s_name, "you are", age, "old and your Eircode is", eircode)

    if eircode[-1] in odd:
        print("You must attend Northfield for your vaccine")

    else:
        print("You must attend Eastwood for your vaccine")
        
    if trial == "Yes" or "yes":
        print("You are now enrolled in the trial to recieve Super vaccine",random.choice(supervaccine))
        
    if age < 50:
        print(f_name, "you will recieve the MRNA vaccine")
        
    if age > 50:
        print(f_name, "you will recieve the ADENO vaccine")
    
    EXIT = input("if you have finished entering people's details type 'END', otherwise press RETURN:")
    if EXIT == "":
        continue
    else:
        break

