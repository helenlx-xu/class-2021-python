if 10<7:
    print('10是大的')
else:
    pass

print('-----判断结束-----')


for i in range(3):
    username = input('请输入用户名:')
    password = input('请输入密码:')
    # 验证用户名和密码
    if username == 'a' and password == '1':
        print('欢迎!用户{}'.format(username))
        print('-------轻松购物吧-------')
        break
    else:
        print('用户名或者密码有误!')
else:
    print('账户被锁定,需要重新激活!')

for i in range(3):
    if i == 1:
        print('这家店是黑店，馒头有毒!!等着关门吧!')
        break
        print('abcd')
    else:
        print('这家店的馒头真香啊!要多吃几个呀!')

print('---->进入消协大门')
