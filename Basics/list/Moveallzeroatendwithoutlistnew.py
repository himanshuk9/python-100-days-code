numbers = [0, 1, 0, 3, 12]

j = 0 

for x in range(len(numbers)):
    if x!=0:
        numbers[j] = numbers[x]
        j = j+1

print(numbers)