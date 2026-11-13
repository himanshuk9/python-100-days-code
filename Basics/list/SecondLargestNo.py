list = [23, 4, 2,5,6]

firstlargest = list[0]
secondlargest = list[1]

for x in list:
    if(firstlargest<x):
        secondlargest = firstlargest
        firstlargest = x

print(secondlargest)