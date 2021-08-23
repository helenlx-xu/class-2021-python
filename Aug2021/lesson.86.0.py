def test(a,b):
    print('---->test enter')
    return a + b

        
def func():
    c = 10
    return c + test(5, 8)

t = func()
print(t)


def test1(i):
    if i == 10:
        return 10
    else:
        return i + test1(i + 1)


r = test1(1)
print(r)