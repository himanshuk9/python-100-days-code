numbers = [3, -1, 4, -2, 0, -5, 7]
newlist = []
for x in numbers:
    if x<0:
        newlist.append(x)

for x in numbers:
    if x>0:
        newlist.append(x)

print(newlist)