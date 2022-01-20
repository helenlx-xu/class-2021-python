movie = '大侦探皮卡丘'
ticket = 45.9
count = 35
total = ticket*count

message ='''
电影：%s
人数：%d
单价：%f
总票价：%.1f

'''
%(movie,count,ticket,total)


print(message)

print('电影：%s'%movie)
print('人数：%d'%count)
print('单价：%.0f'%ticket)
print('总票价：%.1f'%total)