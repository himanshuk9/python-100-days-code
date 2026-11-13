numbers = [4, 5, 4, 1, 4, 5]

for x in numbers:
    countfreq = numbers.count(x)
    if countfreq ==1:
        print(x)
        break