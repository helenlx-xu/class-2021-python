import abc


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)
#从2-29之间一直加三,然后输出

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.
#break已经停止,不会运行后面的代码


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



#以下为自己写的代码
animals = ["cat","dog","tiger"]
for i in animals:
    print(i)


for i in "animals":
    print(i)

for i in range(12):
    print(i)

for i in range(4,5):
    print(i)

for i in range(2, 32, 3):
  print(i)

for i in range(3):
  print(i)
else:
    print("abc")



color = ["red", "yellow", "blue"]
fruits = ["apple", "peach", "banana"]

for i in color:
  for x in fruits:
    print(i, x)
