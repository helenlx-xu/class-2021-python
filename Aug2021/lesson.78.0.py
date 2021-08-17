def test1():
    a = 0
    print('a = ', a)
    a += 10
    print('a = ', a)

def test2():
    pass

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

test1()

a = 10
b = a
c = b

print(id(a))
print(id(b))
print(id(c))

import sys

print(sys.getrefcount(a))