
numbers = [1, 2, 3, 2, 4, 5, 1, 6]

for x in range(len(numbers)):
    for y in range(x + 1, len(numbers)):
        if numbers[x] == numbers[y]:
            print(numbers[x])
            break
