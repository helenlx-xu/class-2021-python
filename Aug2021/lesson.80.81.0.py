def outer():
    a =100

    def inner():
        b = 200
        b += a
        print('我是内部函数',b)

    print(a)
    inner()


outer()

def abc():
    print('********************')
    for i in range(10):
        if i == 6:
            return
        print('---->', i)
    print('####################')
    print('********************')



r = abc
print(r)