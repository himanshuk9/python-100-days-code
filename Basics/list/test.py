numbers = [1, 2, 3, 4, 5]

#  store first the last value :-
k = 2
lastvalue = numbers[-1]

for i in range(len(numbers) -2 , -1 , -1):
    numbers[i+k] = numbers[i]


numbers[k]= lastvalue

print(numbers)
