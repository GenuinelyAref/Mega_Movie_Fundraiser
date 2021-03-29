import random
numbers = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2]
unique_combos = []

for i in range(0, 300000):
    numbers = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2]
    num = ""
    for j in range(0, len(numbers)):
        c = numbers.pop(random.randint(0, len(numbers)-1))
        num += str(c)
    try:
        unique_combos.index(num)
    except ValueError:
        unique_combos.append(num)

print(unique_combos)
print(len(unique_combos))
