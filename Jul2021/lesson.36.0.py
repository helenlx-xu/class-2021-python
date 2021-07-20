s = ' admin '
print(len(s))
result = s.strip()
print(len(result))
print(result)

result = s.lstrip()
print(len(result))
print(result)

result = s.ljust(30)
print(result)

result = s.rjust(30)
print(result)

s = 'hello'+'world'
print(s)

name = '赵丽颖'
age = 18

result = '美女{}今年{}岁'.format(name,age)
print(result)

result = '美女{name}今年{age}岁,我也是{age}岁!'.format(name = '赵丽颖', age = 19)
print(result)