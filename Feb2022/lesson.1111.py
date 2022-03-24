x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

a = 4
A = "Sally"

print(a)
print(A)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#开头不可用数字，中间不能有空格和 -

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

print('----------SECTION 1-------------------------')

x = y = z = "Orange"
print(x)
print(y)
print(z)

print('----------SECTION 2-------------------------')

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print('----------SECTION 3-------------------------')

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print('----------SECTION 4-------------------------')

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print('----------SECTION 5-------------------------')

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print('----------SECTION 6-------------------------')

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


