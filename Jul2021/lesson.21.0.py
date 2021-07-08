a = 1
b = 2
c = a if a<b else b
print(a, b, c)

print('aaaa') if a<b else print('bbbbb')

if a<b:
    print('aaaa')
else:
    print('bbbb')

if '':
    print('11111')
else:
    print('00000')

 

 
'''
循环:
场景:
1.用户名和密码，反复输入
2.计算1-100
3.游戏，死了重生
4. ....

方式:
1.while
2.for

while格式:

whlie 条件：
    要循环执行的代码

布尔类型的条件
'''

n = 1
while n <= 10:
    print('------>n=%d' % n)
    n += 1