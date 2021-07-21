#shoppingcar = []
#while True:
    #name = input('商品名:')
    #price = input('价格:')
    #number = input('数量:')
    #print('清单')

'''
如何定义一个列表: <class 'list'>
1.空列表:[]
2.有内容的列表:['A','B','C'],[1,2,3,4],[3.5,9.9,10],

数据类型:
int: 1,2,3,4,5,6
float: 1.9,2.8 ......
str: ''
bool: True,False
list
'''
List1 = []
List2 = ['牛奶','面包','火腿肠','辣条','臭豆腐','食盐','方便面']

print(List2[0])
print(List2[1])
print(List2[2])
print(List2[3])
print(List2[4])

print(List2[:2])
print(List2[2:4])
print(List2[::-3])
print(List2[-2:-5:-2])
print(List2[::3])