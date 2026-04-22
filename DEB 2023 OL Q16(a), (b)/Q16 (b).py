# Question 16(b)
# Name and School: Sam Moore

flight_number=input("Enter your flight number: ")
list1 = []
list2 = []

if flight_number[-1] == "2":
    list1.append(flight_number)
if flight_number[-1] == "5":
    list2.append(flight_number)

print("Direct flights:",list1)
print("Stopover flights:",list2)