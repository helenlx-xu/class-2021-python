s = 'ABCDEFG'
print(s[1:4])
print(s[0:5])
print(s[:5])

print(s[-3:-1])

x = s[:]
print(x)
print(s)

print(id(x))
print(id(s))

print(s[1:-1])

print('*-' * 20)

print(s[:-1:2])
print(s[1::2])
print(s[::4])

print('**' * 20)
print(s[::-1])
print(s[::])

path = 'https://www.baidu.com/img/dong_e70247ce4b0a3e5ba73e8b3b05429d8f.gif'
i = path.find('_')
print(i)
image_name = path[i+1:]
print(image_name)

i = path.find('#')
print(i)

i = path.rfind('.')
zhui = path[i:]
print(zhui)