'''
阿里巴巴商家节，用户名，消费总金额，账户金额，优惠券
输入总购买金额，
如果金额0 - 500元是lv1级别‘
如果500 - 2000元则是lv2，2000以上是lv3

lv1: 随机赠送3张1 - 10元的优惠券，
lv2: 赠送2张50元的优惠券，如果充值则送充值金额的10%,
lv3: 赠送2张100元的优惠券，如果充值则送充值金额的15%

'''

username = 'Kitty'
total = 1500 # 消费总金额
money = 0 # 账户金额
coupon = 0 # 优惠券

if 0<total<500: # lv1
    # 随机赠送3张1 - 10元的优惠券
    quan1 = random.randint(1,10)
    quan2 = random.randint(1, 10)
    quan3 = random.randint(1, 10)
    #将金额数加到coupon
    coupon = quan1 + quan2 + quan3
elif 500<=total<2000: # lv2
    # 赠送2张50元的优惠券，如果充值则送充值金额的10%
    coupon += 2 * 50
    # 嵌套if
    recharge = input('%s,是否要进行充值(送充值金额的10%)？(y/n)')
    if recharge == 'y':
       money += 1.1*int(input('输入充值金额:'))

elif total>2000: # lv3
    # 赠送2张100元的优惠券，如果充值则送充值金额的15%
    coupon += 2 * 100
    # 嵌套if
    recharge = input('%s,是否要充值(送充值金额的15%)? (y/n)')
    if recharge == 'y':
        money += 1.5*int(input('输入充值金额:'))

n = 9
m = 2
if m > 3:
    print('11111111111111111111')
    if n < 10:
        print('9<10')
    else:
        print('不是9<10')
    print('22222222222222222222')
else:
    print('33333333333333333333')
