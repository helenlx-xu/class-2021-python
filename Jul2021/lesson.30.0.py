s1 = 'hello'
s2 = s1
s3 = 'hello'
s4 = 'hello1'

print(s1,s2,s3)

print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))

print(s1 is s4)

s1 = 'world'

print(s1,s2,s3)
s1 = 'ABCDEFG'

print(s1[6])
print(s1[5])
print(s1[4])
print(s1[3])
print(s1[2])
print(s1[1])
print(s1[0])

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
