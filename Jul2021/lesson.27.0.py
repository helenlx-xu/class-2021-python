import random
coins = 0

if coins < 5:
    print('金币不足请充值再玩！')
while True:
    money = int(input('请输入充值金额：'))
    if money % 10 == 0:
        coins += money //10 * 20
        print('充值成功! 当前金币有%d个' %  coins)

        print('~~~~~~~~~~开启游戏之旅~~~~~~~~~~')
        answer = input('是否开始游戏（y/n)')
        if answer == 'n':
            break
        while coins > 5 and answer == 'y':

            coins -= 5

            coins += 1

            ran1 = random.randint(1,6)
            ran2 = random.randint(1,6)

            guess = input('洗牌完毕，请猜大小：')

            if guess == '大'  and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 <= 6:
                print('恭喜猜对了，你赢了!')
                coins += 2
            else:
                print('很遗憾！本次猜错了！')
                answer = input('是否继续游戏（y/n)')
                if answer == 'n':
                    break
                
    else:
        print('不是十的倍数，充值失败！')
        break