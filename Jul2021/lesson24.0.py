import random
n = 1
p_count = 0
m_count = 0
while n <= 3:
    ran = random.randint(0,2)
    guess = int(input('请输入：剪刀(0) 石头(1) 布(2)\n'))
    if guess == 0 and ran == 2 or guess == 1 and ran == 0 or guess == 2 and ran == 1:
        print('~~~~ 我赢了! ~~~~')
        p_count += 1
    elif ran == 0 and guess == 2 or ran == 1 and guess == 0 or ran == 2 and guess == 1:
        print('~~~~ 机器赢了 ~~~~')
        m_count += 1
    else:
        print('本轮平局! ')