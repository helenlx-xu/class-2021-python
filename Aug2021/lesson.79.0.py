def outer():
    a =100

    def inner():
        b = 200
        b += a
        print('我是内部函数',b)

    print(a)
    inner()


outer()