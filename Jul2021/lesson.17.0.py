n = 12
print(n << 1)
print(n << 2)
print(n << 3)
print(n << 8)

n = 26
print(n << 4)

n = 12
print(n >> 1)
print(n >> 2)
print(n >> 3)
print(n >> 4)
print(n >> 5)

# n = 89  右移5位   结果
# n = 93  左移1位   结果

print(89 >> 5)
print(93 << 3)


print('*'*50)
x = 20
result = 20*5**2
print(result)

a = 1
b = 2

print(b > a + x < a + b)
print(b > a + (x < a + b))
print((b > a) + (x < a + b))

print(a + False)

print(a + True)