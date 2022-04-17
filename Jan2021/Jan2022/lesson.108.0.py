# 赋值运算符

# 1. =
name = 'admin'

# 将'admin'的值赋给 变量name

# 1+1 = 2

name1 = name

print(id(name),name)
print(id(name1),name1)

name2 = name
print(id(name2),name2)

# id()

print(name == name1)  #

print(id(name1),name1)

print(id(name),name)














num = 8

num += 5  # num = num + 5
print(num)

a = 'abc'

a += 'ff'

print(a)

num = 0
num /= 0
print(num)