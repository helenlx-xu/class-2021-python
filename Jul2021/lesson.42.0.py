list1 = ['火腿肠','酸奶','酸奶','辣条','面包','薯条','酸奶']
list1.pop()
print(list1)

list1.pop()
print(list1)

list1.remove('辣条')
print(list1)

if'辣条呀'in list1:
    print('存在')
else:
    print('不存在')

list1.remove('酸奶')
print(list1)

for i in list1:
    if i == '酸奶':
        list1.remove(i)

print(list1)