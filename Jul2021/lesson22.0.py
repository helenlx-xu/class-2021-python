n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1

print('累加和: sum=',sum)

count = 0
while True:
    print('1111111111')
    count += 1
    if count == 5:
        break

total = 0
while True:
    #先买
    price = float(input('输入价格:'))
    number = int(input('输入数量:'))
    #累加
    total += price * number
   
    #判断是否继续购买
    answer = input('当前商品总额: %.2f,是否继续添加商品(q表示退出) ?' % total)
    if answer == 'q':
        # 跳出while循环
        break

print('所有商品的总额是:%.2f' % total)

    