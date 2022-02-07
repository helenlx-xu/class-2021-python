print(2<<1)
print(2>>1)

print(16<<2)

print(16>>2)


# (sanmu)运算符

#格式

# result = (8>10)?'真':'假'(无效语法问题（？）)
# print(result)


'''
判断表达式是True还是False
如果是True则将if前面的内容进行运算，并将结果赋值成result
如果是False则将else后面的内容进行运算，并将结果赋值成result
'''

# 三目正确格式
a = 6
b = 5
result = (a+b)   if a>b else (b-a)

print(result)