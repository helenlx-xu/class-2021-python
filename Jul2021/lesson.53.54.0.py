book = {'书名': '《三体》', '价格': 20, '作者': '刘慈欣'}
value = book.get('书名1','默认')
print(value)

list1 = [1,4,7,8,9]
for i in list1:
    print(input)

for i in book:
    print(i)

book.setdefault('出版社','人民教育出版社')
print(book)

dict1 = {'a':10,'b':20}
book.update(dict1)
print(book)

print(book)
result = dict1.fromkeys(['a','b'],[1,20])

print(result)