'''
查找:
  1. 元素 in 列表      返回booi类型
  2. 列表.index(元素)  返回元素的下标位置，如果没有此元素则报错
  3. 列表.count()     返回整数     返回值是0则表示不存在此元素   存在则返回此元素的个数素在一
'''

list1 = [1,5,4,6,5,9,5]
print(list1.count(5))

list1 = [1,5,4,6,5,9,5]
del list1[3]
print(list1)

list1.pop(3)
print(list1)

list1.clear()
list1.append(1000)
print(list1)

list1 = [1,5,4,6,5,9,5]
print(id(list1))

list2 = list1

list1.append(88)

print(list1)
print(list2)

list1.clear()
print(list2)

del list2

print(list1)