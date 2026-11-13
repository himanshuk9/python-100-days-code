numbers = [12, 0, 0, 9, 16, 3, 8]

new_list = []

for x in numbers:
    if x != 0:
        new_list.append(x)


countzero = len(numbers) - len(new_list)

new_list.extend([0] * countzero)

print(new_list)