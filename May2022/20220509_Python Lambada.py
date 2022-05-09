x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

#下面是自己写的代码

x = lambda a: a + 7
print(x(3))

x = lambda a, b: a * b
print(x(3, 2))

x = lambda a, b, c : a + b + c
print(x(2, 1, 7))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(436781))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(12)) 
print(mytripler(58))
