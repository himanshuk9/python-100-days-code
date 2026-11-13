numbers = [2, 4, 2, 7, 4, 9, 7, 5]


dulpicatelist = []

for x in numbers:
    if x in numbers:
        dulpicatelist.append(x)


print(dulpicatelist)