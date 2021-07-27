
import random
abc_123 = 'qwertyuiopasdfghjklzxcvbnm1234567890qwertyu8i9opASDFGHJKLZXCVBNM'
li = []
for i in range (5):
    s = set()
    while True:
        if len(s) == 4:
            break
        s.add(random.choice(abc_123))
    li.append(s)

print(li)