lst = [10,8,6,4,2]

index = 0
index2 = index + 1
count = 0

while count < 4:
    if lst[index] > lst[index2]:
        save = lst[index]
        lst[index] = lst[index2]
        lst[index2] = save
        
        index += 1
        index2 += 1
        
        count += 1
        print(lst)

index = 0
index2 = index + 1
count = 0
print("\n")

while count < 3:
    if lst[index] > lst[index2]:
        save = lst[index]
        lst[index] = lst[index2]
        lst[index2] = save
        
        index += 1
        index2 += 1
        
        count += 1
        print(lst)
        
index = 0
index2 = index + 1
count = 0
print("\n")

while count < 2:
    if lst[index] > lst[index2]:
        save = lst[index]
        lst[index] = lst[index2]
        lst[index2] = save
        
        index += 1
        index2 += 1
        
        count += 1
        print(lst)

index = 0
index2 = index + 1
count = 0
print("\n")

while count < 1:
    if lst[index] > lst[index2]:
        save = lst[index]
        lst[index] = lst[index2]
        lst[index2] = save
        
        index += 1
        index2 += 1
        
        count += 1
        print(lst)