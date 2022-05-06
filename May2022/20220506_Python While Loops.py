i = 1
while i < 6:
  print(i)
  i += 1



i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#下面是自己写的
a = 2
while a < 3:
    print(a)
    a += 2

a = 3
while a < 10:
    print(a)
    if a == 10:
        break
    a += 1

b = 3
while b < 7:
    b += 1
    if b == 5:
        continue
    print(b)


s = 34
while s < 37:
    print(s)
    s += 1
else:
    print("aystufdwei")