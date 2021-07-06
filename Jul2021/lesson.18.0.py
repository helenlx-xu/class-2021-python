print(1)
print(2)
print(3)

result = input('请输入(y/n):')
if result == 'y':
    print(4)
    print('over~~~~')

print('-----------------')

import random
ran = random.randint(1,10)
print(ran)
...

guess = input('请输入你猜的数:')

if ran == int(guess):
    print('恭喜猜对了 ')
else:
    print('很遗憾猜错了! ')

a = int(input("请输入一个四位整数:"))
if (a // 100 % 10) + (a // 10 % 10) > 10:
    print("success")
else:
    print("fail")

import random
number1 = random.randint(1,10)
number2 = random.randint(1,10)
print(number1,number2)

if number1 + number2 > 8 and (number1 - number2 <= 3 and number2 - number1 <= 3):
    print('success')
else:
    print('fail')

'''
1-5: 1000 元
5-10: 奖励笔记本IBM
10-100: 奖励iphone12
超过了100: 奖励特斯拉
鼓励奖

'''
money = 100000
if 10000 < money <= 50000:
    print('奖励1000元！恭喜！')
elif 50000 < money <= 100000:
    print('奖励笔记本IBM！恭喜！')
elif 100000 < money <= 1000000:
    print('奖励iphone12！恭喜！')
elif money > 1000000:
    print('奖励特斯拉！恭喜！')
else:
    print('鼓励奖，毛绒玩具！')

print('----------欢迎进入人员管理系统----------')
choice = input('请选择功能：\n 1. 添加员工\n 2. 删除员工\n 3. 查询员工\n 4. 修改员工信息\n')
if choice == '1':
    print('添加员工')
elif choice == '2':
    print('删除员工')
elif choice == '3':
    print('查询员工')
elif choice == '4':
    print('修改员工信息')
else:
    print('输入错误！')
