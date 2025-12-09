#5
total5 = 0
y = input('Q5: Enter a number: ')
y = int(y)
y += 1
for x in range(1, y):
    if x % 2 != 0:
        total5 += x
print('Q5', total5)
