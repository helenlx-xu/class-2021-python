from typing import Container


list1 = []
list2 = ['面包']


list1.append('火腿肠')
list1.append('酸奶')
list1.append('辣条')
print(list1)

list2.append('薯条')
print(list2)

list1 = list1 + list2
print(list1)

list1.extend(list2)
print(list1)




container = []
fiag = True
while fiag:

    name = input('商品名称:')
    price = input('商品价格:')
    number = input('商品数量:')
    goods = [name,price,number]

    container.append(goods)

    answer = input('是否继续添加？（按q或Q退出）')
    break
    if answer.lower() == 'q':
        flag = False
