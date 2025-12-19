#step 1
string = input('Enter a card number: ')
string2 = string[:-1:]
checkingnumber=string[-1]
print(string2)

#step 2
string2 = string2[::-1]

#step 3 - odd, even
evenstring = string2[0::2]
oddstring = string2[1::2]
print(evenstring)
print(oddstring)

total1 = 0 #even
total2 = 0 #odd

for x in evenstring:
    x = int(x)
    x *= 2
    if x > 9:
        x -= 9
        total1 += x
    else:
        total1 += x

for x in oddstring:
    x = int(x)
    x *= 2
    if x > 9:
        x -= 9
        total2 += x
    else:
        total2 += x
print(total1)
print(total2)

#step 4 - do as required
total3 = total1 + total2
checkingnumber = int(checkingnumber)
total4 = total3 + checkingnumber
print(total4)

#step 5
if total4 % 10 == 0:
    print('valid card number')
else:
    print('invalid card number')