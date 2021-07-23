

import random
numbers = []
for i in range(8):
    ran = random.randint(1,100)
    numbers.append(ran)
        
print(numbers)




number = int(input("输入一个数字:"))
for i in numbers:
    if number <= i:
        numbers.insert(numbers.index(i),number)
        break
else:
    numbers.append(number)

a = 2
b = 3
print(a,b)

a,b = b,a
print(a,b)

nums = [5,1,7,6,8,2,4,3]
for j in range(0,len(nums) - 1):
    for i in range(0, len(nums) - 1 - j):
        if nums[i] > nums[i + 1]:
            a = nums[i]
            nums[i] = nums[i +1]
            nums[i + 1] = a
print(nums)