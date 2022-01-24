name = 'jack'
name1 = 'jack'

print(id(name))
print(id(name1))

n1 = input('请输入第一个数:')
n2 = input('请输入第二个数:')

result = n1 > n2
# print(result)
print('n1>n2:',result)

result = n1 == n2
print('n1==n2:',result)

m1 = 'hello'
m2 = 'hello'

result = m1 == m2

print('m1==m2:',result)

username = input('输入用户名:')

uname = 'admin123'

result = username == uname

print('用户名的验证结果:',result)   