name = input('请输入名字:')

print(name)

print('''
***********************
      捕鱼达人
***********************
    ''')

username = input('输入参与游戏者用户名:')
password = input('输入密码：')

print('%s请充值才能加入游戏!' % username)


coins = input('请充值：')

print('%s充值成功！当前游戏币是:%d' % (username,coins))