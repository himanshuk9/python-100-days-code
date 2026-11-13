list = [23,34,38,9]

answer = True
for i in range(len(list) -1 ):
    if list[i] > list[i+1]:
        answer = False
        break
     
print(answer)