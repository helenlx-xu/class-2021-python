li = [1,1,1,2,3]

elem = 1
result_li = []
for i in li:
    if i != elem:
        result_li.append(i)

li = result_li
print(li)

list1 = ['火腿肠','酸奶','酸奶','酸奶','辣条','面包','薯条','酸奶']
list1.pop()
list1.pop()
print(list1)

list1.remove('辣条')
print(list1)


list1 = [1,2,3,4,5,6]

weizhi = list1.index(5)

list1[weizhi] = 8
print(list1)

list1 = ['火腿肠','酸奶','酸奶','酸奶','辣条','面包','薯条','酸奶']
t = 0
list.insert(0,str(t))
for i in list:
    if i == '酸奶':
        list.remove(i)
        list.insert(0,str(t))
        t += 1

for i in range(t =1):
    list.remove(list[0])

print9list