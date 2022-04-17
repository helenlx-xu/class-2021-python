'''
变量
运算符
语句:
条件判断语句
for循环语句
跳转语句

条件语句:(判断)
应用场景：
1.用户名和密码登陆
2.用户登录验证(看影院信息，判断用户是否登陆了，没有登陆弹窗口，登陆看到信息)

if 条件：
   条件成立执行的语句
'''

from re import U


username = 'admin' #没有登陆
password = ''
#python:判断的变量’‘ 0 None 默认是False
#python:如果变量有值'abc','kkk','yueryu',认为是True

if username: # ’admin'!='' True  如果条件运算结果是True则进入内层
    print('嘿嘿！我登陆啦!')

print('--------------')



num = 0

if num:
    print('------>',num)



'''
if num:
    print('.....')

等效：

if num!=0:
    print('.....')

'''

'''
如果年龄大于18 并且 输入了姓名，则打印xxx今年xxx岁

'''

age = int(input('输入年龄:'))
username = input('输入用户名')

if age>18 and username:
    print('{}今年{}岁了!'.format(username,age))

print('---game over----')