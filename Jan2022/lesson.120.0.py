'''
应用场景:
1.猜大小  --->反复的猜
2.消消乐  --->反复充值
3.用户登陆 ---->登陆多次
    用户名
    密码

循环结构:
    for 变量名 in 集合:
        语句

怎么用?

'''
# 使用系统给定range()完成范围指定
print(range(8))
# range(0,8)    包含0 但是不包含8   0,1,2,3,4,5,6,7

# 打印三次
for i in range(3):
    print('hello ---->',i)

for i in range(2000):
    print('hello ---->',i)

print('---- game over -----')