#Author: Sam Moore
#Date: 25/11/25
#Assignment: hexa to binary to UTF-8 and vice versa

hexa = input('Enter a Hexadecimal value: U+')
hexa = str(hexa)
power = 0
decimal = 0
#Hexadecimal to decimal

for x in hexa[::-1]:

    if x == 'A':
        x = 10
    elif x == 'B':
        x = 11
    elif x == 'C':
        x = 12
    elif x == 'D':
        x = 13
    elif x == 'E':
        x = 14
    elif x == 'F':
        x = 15
    
    else:
        x = int(x)
        x = x * 16**power
        power += 1
        decimal += x
        continue
    
    
    x = x * 16**power
    power += 1
    decimal += x
        
print(decimal)

#decimal to binary

binary = ' '
while decimal != 0:
    if decimal % 2 == 0:
        binary += '0'

    else:
        decimal -= 1
        binary += '1'
    
    decimal /= 2
print(binary[::-1])