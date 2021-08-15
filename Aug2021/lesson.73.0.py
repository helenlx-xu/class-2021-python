library = ['红楼梦','西游记','水浒传']

def add_book(bookname):
    if bookname not in library:
        library.append(bookname)
    else:
        print('已经存在此书')

def show_book():
    print('图书馆的书籍如下:')
    for book in library:
        print(book)


show_book()