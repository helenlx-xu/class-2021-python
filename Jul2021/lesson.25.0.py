'''
for(....){
    循环体
}

格式:
for 变量名 in range(n):
    循环体中的内容

range(n): 从0开始取值到n-1结束
range(start,stop): [start,stop]
range(start,stop,step): 默认从start(包含)开始取值到stop(不包括)结束，其中步长由step指定, 默认step是1
'''

# 1-10 数字打印
for i in range(10):
    print(i)

print('*' * 50)

for i in range(1,11):
    print('---->',i)

print('*' * 50)

for i in range(1,10,2):
    print('---->',i)

# 1-50 的累加和
sum = 0
for i in range(1,51):
    sum += i
print(sum)

# 最多输入用户名和密码，如果三次没有登录成功，提示账号被锁定
# break 退出
for i in range(3):
    #提示输入用户名和密码
    username = input('用户名:')
    password = input('密码:')
    # 判断输入的是否正确 admin 1234
    if username == 'admin' and password == '1234':
        print('用户登录成功！')
        break
    print('用户名或者密码有误！\n')

if i == 2:
    print('账户被锁定！')