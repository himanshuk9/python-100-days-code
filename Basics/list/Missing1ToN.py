list = [1,2,3,4,6]
asum = 0
for x in list:
    asum = asum+x

n = max(list)
avgsum = n*(n+1)/2

missing = avgsum- asum
print(int(missing))