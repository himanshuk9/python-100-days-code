oldlist = [23,2,3,4,5,6,4,3,2]
newlist  = []

for x in oldlist:
    if x not in newlist:
        newlist.append(x)


print(newlist)