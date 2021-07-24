t1 = ()
print(type(t1))

t2 = ('aa',)
print(type(t2))

t2 = ('aa')
print(type(t2))

t3 = ('a','b','c','a','e','y')
print(type(t3))

print(t2[0])

print(t3[1:])

print(t3[::-1])

n = t3.count('a')
print(n)

index = t3.index('a',1,5)
print(index)