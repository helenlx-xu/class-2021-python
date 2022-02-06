'''
if 判断的第二种使用方式:

if 表达式(条件):
    条件成立
else:
    条件不成立执行的语句

注意:添加缩进 1个tab
'''

'''
需求:
  消消乐
    lv1
    lv2
    ...
lv1:    免费玩 随便玩

lv2:    充值  买道具  继续玩

'''

print('*'*10,'欢迎来到消消乐','*'*10)
level = input('请输入你的级别 (lv1,lv2):')
if level == 'lv1':
    print('免费玩 随便玩')
else:
    print('已经进入付费级别，充值继续玩')
    money = int(input('请充值(必须是100的倍数):'))
    # if 语句是允许嵌套,注意缩进问题
    if money%100 == 0 and money > 0:
        print('充值成功!充值金额是:',money)
    else:
        print('充值失败,充值金额必须是100的倍数!')


'''
if 条件1:
    成立
    if 条件2:
        成立
    else:
        不成立
else:
    不成立
    if 条件3:
        成立
    else:
        不成立

'''
# 随机数:
import random

print(random.randint(1,10))