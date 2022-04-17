sum = 0
for i in range(10):
    if i%3!=0:
        sum += 1
print('sum-----1111->',sum)



sum = 0

for i in range(10):
    if i%3 == 0:
        continue

    sum += 1

print('sum-----2222->,sum')




s1 = 'abc'
s2 = "abc"
s3 = '''
abc
'''
print(id(s1),id(s2),id(s3))

print(s1 == s2)
print(s1 is s2)

print(s2 == s3)
print(s2 is s3)


s1 = input('请输入:')
s2 = input('请输入:')

print(s1 == s2)
print(s1 is s2)

name = 'steven'

result = 'eve' in name
print(result)


result = 'tv' not in name
print(result)