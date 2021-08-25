def test():
    print('------test------')


def func(a, f):
    print('----->', a)
    f()


func(5 ,test)

print('--------------')


def func1(a, f):
    print('++++++++', a)
    r = f(a)
    print('======>', r)


func1(8,lambda x: x ** 2)