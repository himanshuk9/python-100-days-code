list = [12,34,2,4,7] 

firstlarge = float("-inf")
secondlarge = float("-inf")
thirdlarge = float("-inf")

for x in list:
    if x> firstlarge:
        thirdlarge = secondlarge
        secondlarge = firstlarge
        firstlarge = x
    elif x<firstlarge and x>secondlarge:
        secondlarge = x
    elif x<secondlarge and x>thirdlarge:
        x = thirdlarge


print(thirdlarge)