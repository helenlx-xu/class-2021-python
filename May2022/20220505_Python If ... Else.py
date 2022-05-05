a = 33
b = 200
if b > a:
  print("b is greater than a")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")



a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



a = 200
b = 33

if a > b: print("a is greater than b")



a = 2
b = 330
print("A") if a > b else print("B")



a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")




a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")



x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



a = 33
b = 200

if b > a:
  pass
#以下为自己写的代码
a = 123
b = 124
if a > b:
    print('a>b')
elif a == b:
    print('a==b')
else:
    print('a<b')


a = 123
b = 124
if a > b:print('a>b')
elif a == b:print('a==b')
else:print('a<b')

a = 123
b = 124
print('1') if a > b else print('2') if a == b else print('3')


a = 1
b = 2
c = 3
if a < b and b < c:#and指两个条件必须满足
    print('aa')


a = 1
b = 2
c = 3
if a < b or b < c:#or指两个条件满足一个即可
    print('aa')


a = 1
if a > 0:
    print("a")
    if a > 2:
        print("c")
    else:
        print("b")



a = 2
b = 3
if a < b:
    pass