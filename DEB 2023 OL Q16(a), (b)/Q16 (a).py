# Question 16 (a)
# Name and School: Sam Moore

flight_num= input("Enter your flight number: ")
destination= input("Enter your destination: ")
num_ppl= int(input("Enter the number of people in the travel group: "))
children = int(input("Enter the number of children in the travel group: "))

print("Your Flight number is ",flight_num)
print("You are travelling to", destination)
print("There are", num_ppl ,"people in the travel group")

if flight_num == "EI121" or "ei121":
    cost = 250 * num_ppl
if flight_num == "EI125" or "ei125":
    cost = 400 * num_ppl

discount = 50 * children
cost = cost - discount

print("The total cost of your flight is €",cost)