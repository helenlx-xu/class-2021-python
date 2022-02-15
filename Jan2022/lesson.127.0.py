ceng = 1

while ceng <= 5:
    # 打印*
    # print('*)*ceng
    # 嵌套while循环
    count = 1
    while count <= ceng:
        print("'*',end = ''")

        count += 1

    ceng += 1
    print()

print('*'*30)
print('欢迎进入澳门赌场')
print('*'*30)

username = input('请输入顾客大名')
money = 0
answer = input('确定进入游戏吗(y/n)')

if answer == 'y':

    while money < 2:
        n = int(input('金币不足,请充值(100块钱30币,充值必须是100的倍数):'))

        if n%100 == 0 and n > 0:
            money = (n//100)*30

    print('当前剩余游戏币是:{},玩一局扣除2个币'.format(money))

    print('进入游戏...........')

    while Ture:
        
        t1 = random.randint(1,6)
        t2 = random.randint(1,6)