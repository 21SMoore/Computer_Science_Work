list = []
list_input = input("enter a list: ")
list += list_input
count = 0
element = input("enter an element: ")

for x in list:
    if x == element:
        print(x,"is in the list at position",count)
    elif element not in list:
        print("-1")
        break
    else:
        count += 1