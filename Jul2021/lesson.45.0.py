import random

numbers = []
for i in range(8):
    ran = random.randint(1,100)
    numbers.append(ran)

print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)