numbers = [1, 2, 3, 4, 5]

#  store first the last value :-

lastvalue = numbers[-1]

for i in range(len(numbers) -2 , -1 , -1):
    numbers[i+1] = numbers[i]


numbers[0]= lastvalue

print(numbers)
