total = 0
numbers = 0
while True:
    #先买
    price = float(input('输入价格:'))
    number = int(input('输入数量:'))
    #累加
    total += price * number
    #数量累加
    numbers += number
    #判断是否继续购买
    answer = input('当前商品总额: %.2f,是否继续添加商品(q表示退出) ?' % total)
    if answer == 'q':
        # 跳出while循环
        break

print('商品数量共:%d,总额是:%.2f' % (numbers,total))


import random

ran = random.randint(1,50)

while True:
    guess = int(input('猜一个1-50之间的数字:'))
    if guess == ran:
        print('恭喜猜对啦! ')
        break
    elif guess > ran:
        print('猜大了,再小一点!')
    elif guess < ran:
        print('猜小了,再大一点!')

    