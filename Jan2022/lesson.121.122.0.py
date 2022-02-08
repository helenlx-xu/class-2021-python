'''
循环:吃五个馒头

'''
name = '小明'
for i in range(5):
    print('{}很饿,正在吃第{}个馒头'.format(name,i))

print('{}说:终于吃饱啦!'.format(name))

#小明很饿,正在吃第0个馒头 <---- 吃空气
#小明很饿,正在吃第2个馒头
#小明很饿,正在吃第3个馒头
#小明很饿,正在吃第4个馒头
#小明说:终于吃饱啦!

#方法一
name = '小明'
for i in range(1,5):
    print('{}很饿,正在吃第{}个馒头'.format(name,i))

print('{}说:终于吃饱啦!'.format(name))

#小明很饿,正在吃第1个馒头
#小明很饿,正在吃第2个馒头
#小明很饿,正在吃第3个馒头
#小明很饿,正在吃第4个馒头
#小明说:终于吃饱啦!

#方法二
name = '小明'
for i in range(5):
    print('{}很饿,正在吃第{}个馒头'.format(name,i+1))

print('{}说:终于吃饱啦!'.format(name))

#小明很饿,正在吃第1个馒头
#小明很饿,正在吃第2个馒头
#小明很饿,正在吃第3个馒头
#小明很饿,正在吃第4个馒头
#小明很饿,正在吃第5个馒头
#小明说:终于吃饱啦!

# range(n) ---> 0~n-1
# range(m,n) ----> m~n-1


'''
吃馒头:在第三个馒头上抹了一点'鹤顶红'

'''
print('*'*30)
name = '张无忌'
for i in range(1,6):
    #判断i的值是多少,i == 3 别吃
    if i == 3:   # i= 1，2，3，4，5
        print("{}赶快扔掉这个馒头,有剧毒:'鹤顶红'!!!".format(name))
    else:
        print('{}很饿,正在吃第{}个馒头'.format(name,i))

print('{}说:终于吃饱啦!'.format(name))


num = int(input('请输入需要的馒头数量:'))

for i in range(num): # 2
    print('{}很饿,正在吃第{}个馒头'.format(name,i+1))
else:
    print('还没有给我馒头,饿哭啦.....'.format(name))

print('---------------')