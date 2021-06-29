a = 1
b = 2
c = a + b
print(a, b, c)

number = input('请输入一个3位整数: ')
numnber = int(number)

number = int(input('请输入一个3位整数: '))
print('个位数: ', number % 10)
print('十位数: ', number / 10 % 10)


a = 8
b = 4
c = 0

a += 1
print(a, b, c)

b += a
print(a, b, c)

b -= 2
print(a, b, c)

d=3
b //= d
print(a, b, c, d)




a = 10
b = 23

print(a > b)
print(a < b)

print(a == b)
print(a != b)

x = 'abc'
y = 'abcd'

print(x == y)
print(x < y)

c = 10
print(a >= c)

'''
输入考试分数,判断成绩是否在100到80之间？

'''
score = float(input('输入分数:'))
print(80 <= score <= 100)