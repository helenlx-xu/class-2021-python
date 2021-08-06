def show_book(*args,**kwargs):
    print(args)
    print(kwargs)


book = {'bookname': '坏小孩', 'author': 'zzz', 'number': 5}
show_book('龙少', '小芳', s**book)

print(book,'hello,sep='- -')