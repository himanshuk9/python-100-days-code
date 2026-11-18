list1 = [1, 2, 3, 4, 5, 2]
list2 = [2, 4, 6, 8, 4]

newlist = []

for x in list1:
    if x in list2 and x not in  newlist:
        newlist.append(x)


print(newlist)