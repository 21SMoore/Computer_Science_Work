#Author: Samuel Moore
#1/9/25
#Ask the user how many slices of pizza they started with. Then ask them howmany they have eaten. Work out how many are left and display this result to the user

whole_pizza = int(input('How many slices of pizza do you have?: '))
eaten_slices = int(input('How many slices have you eaten?: '))
print('You have this many slices left: ',whole_pizza - eaten_slices)