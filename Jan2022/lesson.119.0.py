'''
猜大小

步骤:
1. 系统产生一个随机数
2. 键盘输入一个数
3. 将系统产生的与键盘输入的进行比较
4. 猜对了,中大奖
   猜错啦  拜拜下次再来

'''
import random


ran = str(random.randint(1,10))
num = input('请输入(1~10)之间的随机:')

if ran == num:
    print('恭喜中大奖了!奖品是:笔记本')
else:
    print('很遗憾你猜错啦!与奖品擦肩而过~~~')


'''
多层条件判断:
if 100-90
    优+
elif 90-80
    优-
elif 80-70
    良
elif 70-60
    及格
else
    不及格


'''

age = int(input('请猜猜宋宋姐年龄:'))

if age<=18 and age>0:
    print('(:-D)[BINGO!]太有眼光啦!')
elif age>18 and age<=30:
    print('人家还是宝宝呢......')
elif age>30 and age<=40:
    print('长得太年轻了吧!!!!')
else:
    print('输入错误!')


