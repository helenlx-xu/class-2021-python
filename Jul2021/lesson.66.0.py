def get_sum(a, b):
    print('函数中:', a, b)
    if isinstance(a, int)and isinstance(b, int):
        s = a + b
        print(s)
    else:
        print('类型错误!')


get_sum(2,3)

get_sum('hello','world')

get_sum('2',3)





def borrow_book(bookname, username, number = 1, school = '1000phone'):
    print('进入借书系统....')
    print('{}要借阅的书名是:{},借阅的数量:{}'.format(username, bookname, number))


borrow_book('狂人日记', '小芳')

borrow_book('草房子', '小明', school = '北科')

borrow_book('西游记', '小红', 5)

borrow_book(username = '小明', bookname = '水浒传')