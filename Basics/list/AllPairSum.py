list = [12,34,2,4,7] 

target = 6

for x in range(len(list) -1):
    for y in range(x+1 , len((list))):
        if list[x] + list[y] == target:
            print(list[x] , list[y])